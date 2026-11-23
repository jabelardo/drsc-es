#!/usr/bin/env python3
"""Build js/generador-personajes.js (the Cap. 2 character sentence generator) from DRSC-ES.html.

The script collects the core descriptors (Cap. 4), the four core types (Cap. 3), the flavors
(Cap. 5), every focus (Cap. 6) and the sample character arcs (Cap. 10), with the id each one
links to, and writes them into the generator script. Re-run it after adding descriptors,
flavors, foci or arcs. Each arc also needs a first-person phrase in FRASES_ARCOS (after OG-CSRD's
generator); the build fails if an arc has none.

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


# First-person phrase for each sample arc, after the OG-CSRD generator ("I must Avenge someone or
# something"). Keyed by the arc's id; the text in [brackets] links to the arc.
FRASES_ARCOS = {
    'aprender': 'Quiero [aprender] algo nuevo',
    'ayudar-a-un-amigo': 'Quiero [ayudar a un amigo]',
    'ayudar-a-una-organizacion': 'Me propongo [ayudar a una organización]',
    'caer-en-desgracia': 'Temo [caer en desgracia]',
    'construccion-1': 'Quiero levantar una [construcción] que perdure',
    'convertirse-en-defensor': 'Voy a [convertirme en defensor] de quienes lo necesitan',
    'creacion': 'Trabajo en mi mayor [creación]',
    'crecimiento': 'No puedo seguir así. Me llega la hora del [crecimiento] y del cambio',
    'criar-a-un-ni~o': 'Tengo que [criar a un niño]',
    'defensa': 'Organizaré la [defensa] de algo importante',
    'derrotar-a-un-enemigo': 'Debo [derrotar a un enemigo]',
    'desarrollar-estrategias-de-afrontamiento': 'Debo [desarrollar estrategias de afrontamiento] para lo que he vivido',
    'desarrollar-un-vinculo': 'Busco [desarrollar un vínculo] con otra persona',
    'descubrir-un-secreto': 'Me cansé de las mentiras y quiero [descubrir un secreto]',
    'deshacer-un-agravio': 'Debo [deshacer un agravio] del pasado',
    'echar-raices': 'Por fin ha llegado el momento de asentarme y [echar raíces]',
    'empresa': 'Quiero montar mi propia [empresa]',
    'entrenar-a-una-criatura': 'Debo [entrenar a una criatura]',
    'explorar': 'Quiero [explorar] con audacia lo desconocido',
    'instruir': 'Hay alguien en mi vida a quien debo [instruir]',
    'justicia': 'Debo traer algo de [justicia] a este mundo',
    'nacimiento': 'Me preparo para un [nacimiento] en la familia',
    'nuevo-descubrimiento': 'Quiero hacer un [nuevo descubrimiento]',
    'pagar-una-deuda': 'Debo [pagar una deuda]',
    'pasado-misterioso': 'Quiero saber más de mi [pasado misterioso]',
    'perfeccionar-una-habilidad': 'Voy a [perfeccionar una habilidad] y a estar entre los mejores de los mejores',
    'purificacion': 'Debo lograr la [purificación] de alguien o de algo',
    'reconocimiento': 'Quiero [reconocimiento]: quiero que se fijen en mí',
    'recuperarse-de-una-herida-o-trauma': 'Necesito [recuperarme de una herida (o trauma)]',
    'redencion': 'Busco mi [redención]',
    'rescate': 'Debo ir al [rescate] de alguien o de algo que me importa',
    'resolver-un-misterio': 'Intento [resolver un misterio]',
    'restauracion': 'Quiero recuperar mi antigua vida. Busco la [restauración]',
    'revancha': 'Quiero tomarme la [revancha]',
    'robo': 'Planeo el [robo] de algo importante',
    'romance': 'Quiero un [romance] en mi vida',
    'terminar-una-gran-obra': 'Recibí el legado de los siglos. Voy a [terminar una gran obra]',
    'tomar-el-camino-equivocado': 'Estoy a punto de [tomar el camino equivocado]',
    'transformacion': 'Debo atravesar una [transformación] radical',
    'unirse-a-una-organizacion': 'Aspiro a [unirme a una organización]',
    'venganza': 'Debo cobrar [venganza] por alguien o por algo',
}


def frases_arcos(arcos):
    """[link text, id, text before, text after] for each arc, from FRASES_ARCOS."""
    ids = [a[1] for a in arcos]
    missing = [i for i in ids if i not in FRASES_ARCOS]
    stale = [i for i in FRASES_ARCOS if i not in ids]
    if missing or stale:
        sys.exit(f'FRASES_ARCOS out of step with the arcs: missing {missing}, unknown {stale}')
    out = []
    for i in ids:
        m = re.fullmatch(r'([^\[\]]*)\[([^\[\]]+)\]([^\[\]]*)', FRASES_ARCOS[i])
        if not m:
            sys.exit(f'FRASES_ARCOS[{i!r}] needs exactly one [linked] part')
        out.append([m.group(2), i, m.group(1), m.group(3)])
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
    arcos = frases_arcos(arcos)
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
    arco: () => {
      const a = pick(D.arcos);
      put('gen-out-arco', a[2], link(a, false), a[3]);
    },
  };
  function init() {
    for (const [key, fn] of Object.entries(parts)) {
      const b = document.getElementById('gen-' + key);
      if (b) b.addEventListener('click', fn);
    }
    // As in OG-CSRD, a random sentence has an aspect 2 times in 5; the button always adds one.
    const all = () => {
      parts.descriptor();
      parts.tipo();
      if (Math.random() * 5 < 2) parts.aspecto();
      else put('gen-out-aspecto');
      parts.rasgo();
      parts.arco();
    };
    const todo = document.getElementById('gen-todo');
    if (todo) todo.addEventListener('click', all);
    all(); // pre-load a sentence, as OG-CSRD does
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
