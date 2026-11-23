#!/usr/bin/env python3
"""Render DRSC-ES.html (or one section of it) in headless Chrome, in the light and/or
dark theme, save screenshots and report browser console messages.

A section is rendered as a stand-alone page that holds the section's lines inside the
same part container, so part colours and styles apply. Headless Chrome does not
scroll to #anchors, so this is how a section deep in the page gets checked.

Usage:
  python3 tools/qa/render.py [--file DRSC-ES.html] [--section ID] [--lines N]
                             [--theme light|dark|both] [--out DIR] [--size WxH]

Chrome is taken from $CHROME, else google-chrome / chromium on PATH, else the
Flatpak apps com.google.Chrome or org.chromium.Chromium.

Exit status: 1 if Chrome fails or the console shows anything other than the known
file:// manifest message, else 0.
"""
import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

IGNORED_CONSOLE = [
    re.compile(r"Access to manifest at 'file://.*' from origin 'null' has been blocked by CORS policy"),
    # headless Chrome probing the GPU on a full-page render; the page uses no WebGL or WebGPU
    re.compile(r"Automatic fallback to software WebGL has been deprecated"),
    re.compile(r"^No available adapters\.$"),
]
ASSET_DIRS = ('css', 'js', 'icon', 'quickref/assets')  # quickref/assets: the difficulty dial in Cap. 11


def find_chrome(explicit):
    if explicit:
        return [explicit], False
    if os.environ.get('CHROME'):
        return [os.environ['CHROME']], False
    for name in ('google-chrome', 'google-chrome-stable', 'chromium', 'chromium-browser'):
        p = shutil.which(name)
        if p:
            return [p], False
    if shutil.which('flatpak'):
        for app in ('com.google.Chrome', 'org.chromium.Chromium'):
            if subprocess.run(['flatpak', 'info', app], capture_output=True).returncode == 0:
                return ['flatpak', 'run', app], True
    sys.exit('error: no Chrome or Chromium found; set CHROME=/path/to/chrome')


def theme_script(theme):
    return ("<script>try{localStorage.setItem('lightSwitch','%s')}catch(e){}</script>" % theme)


def build_page(src_lines, section, nlines, theme):
    head_end = next(i for i, s in enumerate(src_lines) if '</head>' in s)
    if section is None:
        out = list(src_lines)
        out.insert(head_end, theme_script(theme))
        return '\n'.join(out)
    pat = re.compile(r'<[^>]*\bid="%s"' % re.escape(section))
    hits = [i for i, s in enumerate(src_lines) if pat.search(s)]
    if not hits:
        sys.exit(f'error: no element with id="{section}"')
    a = hits[0]
    part = 'part0'
    for j in range(a, -1, -1):
        m = re.search(r'<div id="(part\d+)"', src_lines[j])
        if m:
            part = m.group(1)
            break
    body = src_lines[a:a + nlines]
    body_tag = next((s for s in src_lines if s.lstrip().startswith('<body')), '<body class="theme-light">')
    return '\n'.join(
        src_lines[:head_end] + [theme_script(theme), '</head>', body_tag.strip(),
                                '<div class="container-xxl rounded-3 mt-1 mb-1 print-across" id="drsc-es-content">',
                                '<main class="ps-3">',
                                '<div id="%s"><input type="checkbox" id="lightSwitch" hidden>' % part]
        + body + ['</div></main></div>', '<script src="js/modeswitch.js"></script>', '</body></html>'])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--file', default='DRSC-ES.html')
    ap.add_argument('--section', help='id of the heading (or element) to start from')
    ap.add_argument('--lines', type=int, default=150, help='source lines to include for --section')
    ap.add_argument('--theme', choices=('light', 'dark', 'both'), default='both')
    ap.add_argument('--out', help='directory for the screenshots (default: a new temporary directory)')
    ap.add_argument('--size', default='1280x1600', help='window size, WIDTHxHEIGHT')
    ap.add_argument('--chrome', help='path to the Chrome binary')
    args = ap.parse_args()

    src = Path(args.file).resolve()
    root = src.parent
    lines = src.read_text(encoding='utf-8').split('\n')
    out_dir = Path(args.out).resolve() if args.out else Path(tempfile.mkdtemp(prefix='drsc-render-'))
    out_dir.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix='drsc-page-'))
    for d in ASSET_DIRS:
        if (root / d).is_dir():
            shutil.copytree(root / d, work / d)
    for f in ('manifest.json',):
        if (root / f).exists():
            shutil.copy(root / f, work / f)

    chrome, is_flatpak = find_chrome(args.chrome)
    w, h = args.size.lower().split('x')
    themes = ('light', 'dark') if args.theme == 'both' else (args.theme,)
    name = args.section or 'page'
    failed = False
    for theme in themes:
        page = work / f'{name}-{theme}.html'
        page.write_text(build_page(lines, args.section, args.lines, theme), encoding='utf-8')
        shot = out_dir / f'{name}-{theme}.png'
        profile = Path(tempfile.mkdtemp(prefix='drsc-profile-', dir=work))
        cmd = list(chrome)
        if is_flatpak:
            cmd[2:2] = [f'--filesystem={work}', f'--filesystem={out_dir}']
        cmd += ['--headless=new', '--disable-gpu', '--no-first-run', '--hide-scrollbars',
                f'--user-data-dir={profile}', f'--window-size={w},{h}', '--virtual-time-budget=8000',
                '--enable-logging=stderr', '--v=0', f'--screenshot={shot}', page.as_uri()]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        except subprocess.TimeoutExpired:
            print(f'[{theme}] Chrome timed out')
            failed = True
            continue
        console = [m.group(1) for m in re.finditer(r'CONSOLE[^\]]*\]\s*"(.*?)", source:', r.stderr)]
        unexpected = [c for c in console if not any(p.search(c) for p in IGNORED_CONSOLE)]
        ok = shot.exists() and shot.stat().st_size > 0
        print(f'[{theme}] {"saved " + str(shot) if ok else "no screenshot (exit " + str(r.returncode) + ")"}; '
              f'console: {len(unexpected)} unexpected message(s)')
        for c in unexpected:
            print('    ' + c[:300])
        failed |= (not ok) or bool(unexpected)
    shutil.rmtree(work, ignore_errors=True)
    print('FAIL' if failed else 'OK')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
