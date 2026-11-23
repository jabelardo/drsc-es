#!/usr/bin/env python3
"""Download and tone the book's illustrations (book/assets/arte/) from book/arte/fuentes.json.

Every file must be public domain or CC0 on Wikimedia Commons (checked through the Commons API;
anything else is refused). Each image is toned as a duotone in its part's colour, as the book's
chapter-end art, and the manifest gets the licence and source for the credits page (title, author and date are drafted
from the Commons metadata when missing; edit them in the manifest, reruns keep them).
Optional tool: needs Pillow (pip install pillow) and network access. The book build only reads the
results, which are kept in the repository.

Usage: python3 book/arte/preparar.py [--solo CAPITULO]
"""
import argparse, io, json, os, re, time, urllib.error, urllib.parse, urllib.request
from pathlib import Path
from PIL import Image, ImageOps

RAIZ = Path(__file__).resolve().parent
MANIFIESTO = RAIZ / 'fuentes.json'
SALIDA = RAIZ.parent / 'assets' / 'arte'
# Wikimedia asks automated clients for contact details in the User-Agent and rate-limits those
# without them: set WIKIMEDIA_CONTACT (an email or URL of your own) when you run this tool.
UA = {'User-Agent': 'drsc-es-book-art/1.0' + (f" ({os.environ['WIKIMEDIA_CONTACT']})" if os.environ.get('WIKIMEDIA_CONTACT') else '')}
# part colours of the book (plantilla.typ): dark ink and tinted paper for each duotone
OSCUROS = ['#330033', '#003366', '#663300', '#554411', '#114422', '#222244', '#660000']
CLAROS = ['#f6eef4', '#eef2fa', '#faf1ea', '#f7f4e8', '#edf6ef', '#efeff8', '#f9ecec']
LICENCIAS = ('public domain', 'cc0', 'pd')
LADO = 1280          # a standard thumbnail width, usually cached by Wikimedia
PAUSA = 10 if os.environ.get('WIKIMEDIA_CONTACT') else 60   # seconds between files (Wikimedia rate-limits bursts)
MAX_ORIGINAL = 30_000_000   # originals up to this size are downloaded and scaled here; larger ones use the thumbnail


def api(titulo):
    q = urllib.parse.urlencode(dict(action='query', titles=titulo, prop='imageinfo', iiprop='url|size|extmetadata',
                                    iiurlwidth=LADO, format='json'))
    r = json.load(urllib.request.urlopen(urllib.request.Request('https://commons.wikimedia.org/w/api.php?' + q, headers=UA), timeout=60))
    return next(iter(r['query']['pages'].values()))['imageinfo'][0]


def bajar(url, intentos=30):
    for k in range(intentos):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180).read()
        except urllib.error.HTTPError as err:
            if err.code != 429 or k == intentos - 1:
                raise
            espera = int(err.headers.get('Retry-After') or 120) + 15
            print(f'  429, retrying in {espera} s', flush=True)
            time.sleep(espera)


def limpio(html):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', html or '')).strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--solo')
    a = ap.parse_args()
    lista = json.loads(MANIFIESTO.read_text(encoding='utf-8'))
    SALIDA.mkdir(parents=True, exist_ok=True)
    for e in lista:
        if a.solo and e['capitulo'] != a.solo:
            continue
        if not a.solo and 'imagen' in e and (RAIZ.parent.parent / e['imagen'].lstrip('/')).exists():
            continue                    # already done (rerun to resume after a rate limit)
        info = api(e['archivo'])
        md = info.get('extmetadata', {})
        lic = limpio(md.get('LicenseShortName', {}).get('value'))
        if not lic.lower().startswith(LICENCIAS):
            raise SystemExit(f"{e['archivo']}: licence {lic!r} is not public domain or CC0")
        # originals are served from the CDN; Wikimedia's thumbnail renderer rate-limits much sooner
        usar_original = info.get('size', 0) <= MAX_ORIGINAL
        datos = bajar(info['url'] if usar_original else (info.get('thumburl') or info['url']))
        Image.MAX_IMAGE_PIXELS = None
        im = Image.open(io.BytesIO(datos)).convert('L')
        im.thumbnail((LADO, LADO))
        im = ImageOps.autocontrast(im, cutoff=1)
        p = e['parte']
        im = ImageOps.colorize(im, black=OSCUROS[p], white=CLAROS[p], mid=None)
        clave = re.sub(r'[^a-z0-9]+', '-', e['capitulo'].replace('~', 'n')).strip('-')
        destino = SALIDA / f'{clave}.jpg'
        im.save(destino, quality=80, optimize=True, progressive=True)
        e.update(imagen=f'/book/assets/arte/{clave}.jpg', ancho=im.width, alto=im.height, licencia=lic,
                 fuente='https://commons.wikimedia.org/wiki/' + urllib.parse.quote(e['archivo'].replace(' ', '_')))
        # credits: Commons metadata only as a first draft; edited values in the manifest are kept
        e.setdefault('obra', limpio(md.get('ObjectName', {}).get('value')) or e['archivo'][5:].rsplit('.', 1)[0])
        e.setdefault('autor', limpio(md.get('Artist', {}).get('value'))[:120])
        e.setdefault('fecha', limpio(md.get('DateTimeOriginal', {}).get('value'))[:40])
        print(f"{clave}: {im.width}x{im.height} {destino.stat().st_size // 1024} KB, {lic}", flush=True)
        MANIFIESTO.write_text(json.dumps(lista, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        time.sleep(PAUSA)


if __name__ == '__main__':
    main()
