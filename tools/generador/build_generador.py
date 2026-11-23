#!/usr/bin/env python3
"""Build js/generador-personajes.js (the Cap. 2 character sentence generator) from DRSC-ES.html.

The script collects the core descriptors (Cap. 4), the four core types (Cap. 3), the flavors
(Cap. 5), every focus (Cap. 6) and the sample character arcs (Cap. 10), with the id each one
links to, and writes them into the generator script. Re-run it after adding descriptors,
flavors, foci or arcs.

Usage: python3 tools/generador/build_generador.py [--es DRSC-ES.html] [--out js/generador-personajes.js] [--check]
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def clean(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()


def chapter(t, h3):
    s = t.index(f'<h3 id="{h3}"')
    e = t.index('<h3', s + 10)
    return t[s:e]


def bracketed(seg, levels):
    """Headings 'Nombre [English]' at the given levels: (name, id), preferring the inner span id."""
    out = []
    for m in re.finditer(r'<h(%s)[^>]*\bid="([^"]+)"[^>]*>(.*?)</h\1>' % levels, seg, re.S):
        body = m.group(3)
        span = re.search(r'<span id="([^"]+)"></span>', body)
        title = clean(re.sub(r'<span class="float-end">.*?</span>|<a class="drsc-es-header-anchor".*?</a>', '', body))
        b = re.match(r'(.*?)\s*\[[^\]]*[A-Za-z][^\]]*\]', title)
        if b and b.group(1):
            out.append([b.group(1).strip(), span.group(1) if span else m.group(2)])
    return out


def build(t):
    desc = bracketed(chapter(t, 'descriptores-de-personaje'), '5|6')
    tipos = [['Guerrero', 'guerrero'], ['Adepto', 'adepto'], ['Explorador', 'explorador'], ['Orador', 'orador']]
    asp = chapter(t, 'seleccionar-aspecto')
    aspectos = [[clean(re.sub(r'<a class="drsc-es-header-anchor".*?</a>', '', m.group(2))), m.group(1)]
                for m in re.finditer(r'<h4[^>]*\bid="([^"]+)"[^>]*>(.*?)</h4>', asp, re.S)
                if not m.group(1).startswith(('referencia-rapida', 'regla-opcional'))]
    rasgos = bracketed(chapter(t, 'seleccionar-rasgo'), '5')
    s = t.index('id="ejemplos-de-arcos-de-personaje"')
    e = re.compile(r'<h3[\s>]|<h4(?![^>]*id="referencia-rapida)[^>]*>').search(t, s + 10)
    arcs_seg = t[s:e.start()]
    arcos = [[clean(re.sub(r'<a class="drsc-es-header-anchor".*?</a>', '', m.group(2))), m.group(1)]
             for m in re.finditer(r'<h5[^>]*\bid="([^"]+)"[^>]*>(.*?)</h5>', arcs_seg, re.S)]
    for name, lst in [('descriptores', desc), ('aspectos', aspectos), ('rasgos', rasgos), ('arcos', arcos)]:
        assert lst, name
    return {'descriptores': desc, 'tipos': tipos, 'aspectos': aspectos, 'rasgos': rasgos, 'arcos': arcos}


JS = """// Generador de frases de personaje (Cap. 2). Generado por tools/generador/build_generador.py; no editar a mano.
(function () {
  const D = __DATA__;
  const pick = (a) => a[Math.floor(Math.random() * a.length)];
  const lower = (s) => s.charAt(0).toLowerCase() + s.slice(1);
  function link(entry, low) {
    const a = document.createElement('a');
    a.href = '#' + entry[1];
    a.textContent = low ? lower(entry[0]) : entry[0];
    return a;
  }
  function put(id, ...nodes) {
    const el = document.getElementById(id);
    if (el) el.replaceChildren(...nodes);
  }
  const parts = {
    descriptor: () => put('gen-out-descriptor', link(pick(D.descriptores), true)),
    tipo: () => put('gen-out-tipo', link(pick(D.tipos), true)),
    aspecto: () => put('gen-out-aspecto', ' con aspecto de ', link(pick(D.aspectos), true)),
    rasgo: () => put('gen-out-rasgo', link(pick(D.rasgos), true)),
    arco: () => put('gen-out-arco', link(pick(D.arcos), false)),
  };
  function init() {
    for (const [key, fn] of Object.entries(parts)) {
      const b = document.getElementById('gen-' + key);
      if (b) b.addEventListener('click', fn);
    }
    const all = document.getElementById('gen-todo');
    if (all) all.addEventListener('click', () => Object.values(parts).forEach((fn) => fn()));
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--es', default=str(ROOT / 'DRSC-ES.html'))
    ap.add_argument('--out', default=str(ROOT / 'js' / 'generador-personajes.js'))
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    data = build(Path(a.es).read_text(encoding='utf-8'))
    js = JS.replace('__DATA__', json.dumps(data, ensure_ascii=False, indent=2))
    out = Path(a.out)
    if a.check:
        ok = out.exists() and out.read_text(encoding='utf-8') == js
        print('up to date' if ok else 'out of date')
        sys.exit(0 if ok else 1)
    out.write_text(js, encoding='utf-8')
    print('wrote', out, {k: len(v) for k, v in data.items()})


if __name__ == '__main__':
    main()
