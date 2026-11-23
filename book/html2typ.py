#!/usr/bin/env python3
"""Convert DRSC-ES.html into Typst content for the book PDF (book/build/contenido.typ).

The output only calls the components defined in book/plantilla.typ (parte, capitulo, encabezado,
ficha, recuadro, lateral, refrapida, tabla, ...), so the look of the book lives in the template.
Every HTML id becomes a Typst label; links to ids that are not in the output become plain text.

Usage: python3 book/html2typ.py [--es DRSC-ES.html] [--out book/build/contenido.typ]
"""
import argparse
import re
from html.parser import HTMLParser
from pathlib import Path

VOID = {'br', 'img', 'hr', 'input', 'meta', 'link', 'source', 'wbr', 'col', 'path', 'polygon', 'rect', 'circle'}
SKIP = {'script', 'style', 'svg', 'button', 'input', 'select', 'label', 'form', 'nav', 'textarea', 'option'}


class Node:
    __slots__ = ('tag', 'attrs', 'children', 'parent')

    def __init__(self, tag, attrs=None, parent=None):
        self.tag, self.attrs, self.children, self.parent = tag, dict(attrs or {}), [], parent

    def cls(self):
        return set((self.attrs.get('class') or '').split())

    def text(self):
        return ''.join(c if isinstance(c, str) else c.text() for c in self.children)


class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node('root')
        self.cur = self.root

    CLOSES_P = {'address', 'article', 'aside', 'blockquote', 'div', 'dl', 'fieldset', 'footer', 'form', 'h1', 'h2', 'h3',
                'h4', 'h5', 'h6', 'header', 'hr', 'nav', 'ol', 'p', 'pre', 'section', 'table', 'ul'}
    SCOPE = {'root', 'html', 'body', 'table', 'td', 'th', 'button'}
    SIBLINGS = {'li': ({'li'}, {'ul', 'ol'}), 'dt': ({'dt', 'dd'}, {'dl'}), 'dd': ({'dt', 'dd'}, {'dl'}),
                'tr': ({'tr'}, {'table', 'thead', 'tbody', 'tfoot'}), 'td': ({'td', 'th'}, {'tr', 'table'}),
                'th': ({'td', 'th'}, {'tr', 'table'}), 'thead': ({'tbody', 'thead'}, {'table'}), 'tbody': ({'tbody', 'thead'}, {'table'})}

    def close_open(self, names, stop):
        """Implied end tags (as browsers do): close the nearest open element in `names` unless a `stop` element comes first."""
        n = self.cur
        while n is not self.root and n.tag not in stop:
            if n.tag in names:
                self.cur = n.parent
                return
            n = n.parent

    def handle_starttag(self, tag, attrs):
        if tag in self.CLOSES_P:
            self.close_open({'p'}, self.SCOPE)
        if tag in self.SIBLINGS:
            names, stop = self.SIBLINGS[tag]
            self.close_open(names, stop | self.SCOPE - {'table', 'td', 'th'} if tag in ('li', 'dt', 'dd') else stop)
        n = Node(tag, attrs, self.cur)
        self.cur.children.append(n)
        if tag not in VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, attrs, self.cur))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.children.append(data)


ESC = re.compile(r'([\\#*_`$<>@\[\]~/=+\-])')


def esc(s):
    return ESC.sub(r'\\\1', s)


def q(s):
    """A Typst string literal."""
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def lab(i):
    return f'#label({q(i)})'


class Converter:
    def __init__(self, known):
        self.known = known          # ids that the output will define (filled by a dry run)
        self.emitted = set()
        self.part = 0

    # ---------- inline ----------
    def inline(self, node, strip_float=False):
        out = []
        for c in node.children:
            if isinstance(c, str):
                out.append(esc(re.sub(r'\s+', ' ', c)))
                continue
            t, cl = c.tag, c.cls()
            if t in SKIP or 'drsc-es-header-anchor' in cl:
                continue
            if t == 'span' and 'float-end' in cl and strip_float:
                continue
            if c.attrs.get('id') and t in ('span', 'a', 'strong', 'em'):
                out.append(self.anchor(c.attrs['id']))
            if t == 'a':
                href = c.attrs.get('href', '')
                inner = self.inline(c).strip()
                if not inner:
                    continue
                if href.startswith('#') and href[1:] in self.known:
                    out.append(f'#link(label({q(href[1:])}))[{inner}]')
                elif href.startswith(('http://', 'https://', 'mailto:')):
                    out.append(f'#link({q(href)})[{inner}]')
                elif href and not href.startswith('#'):
                    out.append(f'#link({q("https://jabelardo.github.io/drsc-es/" + href)})[{inner}]')
                else:
                    out.append(inner)
            elif t in ('strong', 'b'):
                inner = self.inline(c).strip()
                if inner:
                    out.append(f'#strong[{inner}]')
            elif t in ('em', 'i'):
                inner = self.inline(c).strip()
                if inner:
                    out.append(f'#emph[{inner}]')
            elif t == 'br':
                out.append('#linebreak() ')
            elif t == 'span' and 'd-block' in cl:
                out.append('#linebreak() ' + self.inline(c).strip())
            elif t == 'span' and 'text-uppercase' in cl:
                out.append(f'#upper[{self.inline(c).strip()}]')
            elif t in ('sup',):
                out.append(f'#super[{self.inline(c)}]')
            elif t in ('sub',):
                out.append(f'#sub[{self.inline(c)}]')
            elif t == 'small':
                out.append(f'#text(size: 0.85em)[{self.inline(c)}]')
            elif t == 'img':
                continue
            else:
                out.append(self.inline(c, strip_float))
        return ''.join(out)

    def anchor(self, i):
        self.emitted.add(i)
        return f'#metadata(none){lab(i)}'

    def clean(self, s):
        return re.sub(r'\s+', ' ', s).strip()

    # ---------- blocks ----------
    def blocks(self, node):
        out = []
        buf = []                     # loose inline content between blocks

        def flush():
            s = self.clean(''.join(buf))
            buf.clear()
            if s:
                out.append(s)
        for c in node.children:
            if isinstance(c, str):
                buf.append(esc(re.sub(r'\s+', ' ', c)))
                continue
            if c.tag in SKIP or 'drsc-es-header-anchor' in c.cls():
                continue
            if c.tag in ('a', 'strong', 'b', 'em', 'i', 'span', 'small', 'sup', 'sub', 'br') and not has_block(c):
                wrap = Node('x'); wrap.children = [c]
                buf.append(self.inline(wrap))
                continue
            flush()
            r = self.block(c)
            if r:
                out.append(r)
        flush()
        return out

    def join(self, parts):
        return '\n'.join(p for p in parts if p)

    def block(self, n):
        t, cl, i = n.tag, n.cls(), n.attrs.get('id')
        pre = self.anchor(i) + '\n' if i and t not in ('h2', 'h3', 'h4', 'h5', 'h6', 'table') else ''
        if t == 'p' and find(n, lambda x: x.attrs.get('id', '').startswith('gen-out-')) is not None:
            return ''                # the generator's output lines only make sense on the web
        if t == 'p':
            s = self.clean(self.inline(n))
            if not s:
                return pre.strip()
            if 'h6' in cl or 'heading' in cl:
                return pre + f'#rotulo[{s}]'
            if 'text-center' in cl or 'lead' in cl:
                return pre + f'#align(center)[{s}]'
            return pre + s + '\n'
        if t in ('h2', 'h3', 'h4', 'h5', 'h6'):
            return self.heading(n)
        if t in ('ul', 'ol'):
            return pre + self.lista(n)
        if t == 'table':
            return self.tabla(n)
        if t == 'dl':
            items, cur = [], None
            for c in n.children:
                if isinstance(c, Node) and c.tag == 'dt':
                    cur = [self.clean(self.inline(c)), '']
                    items.append(cur)
                elif isinstance(c, Node) and c.tag == 'dd' and cur is not None:
                    cur[1] = self.join(self.blocks(c))
            return pre + '#terminos((' + ''.join(f'([{a}], [{b}]),' for a, b in items) + '))'
        if t == 'div' and any(isinstance(c, Node) and c.tag == 'button' for c in n.children):
            return '#generador-web()'
        if t == 'div':
            inner = self.join(self.blocks(n))
            if 'alert' in cl:
                return pre + f'#recuadro[\n{inner}\n]'
            if 'drsc-es-sidebar' in cl or 'drsc-es-ednote' in cl:
                return pre + f'#lateral[\n{inner}\n]'
            if 'drsc-es-dial' in cl:
                return pre + '#dial()'
            if 'ratio' in cl:
                f = next((c for c in n.children if isinstance(c, Node) and c.tag == 'iframe'), None)
                if f is not None:
                    url = f.attrs.get('src', '').replace('/embed/', '/watch?v=')
                    return pre + f'#video({q(f.attrs.get("title", "Vídeo"))}, {q(url)})'
                return pre
            return pre + inner
        if t == 'iframe':
            return ''
        if t == 'hr':
            return ''
        if t in ('section', 'article', 'blockquote', 'li', 'dd', 'dt'):
            return pre + self.join(self.blocks(n))
        return pre + self.join(self.blocks(n))

    def heading_text(self, n):
        """Heading content without its anchor, chapter label and level span; extra ids become anchors."""
        aliases, label, level = [], None, None
        for c in n.children:
            if isinstance(c, Node):
                cl = c.cls()
                if c.tag == 'span' and 'drsc-es-chapter' in cl:
                    label = self.clean(c.text())
                elif c.tag == 'span' and 'float-end' in cl:
                    level = self.clean(c.text())
                elif c.tag == 'span' and c.attrs.get('id') and not c.children:
                    aliases.append(c.attrs['id'])
        wrap = Node('x')
        wrap.children = [c for c in n.children if not (isinstance(c, Node) and (
            'drsc-es-chapter' in c.cls() or 'float-end' in c.cls() or (c.tag == 'span' and c.attrs.get('id') and not c.children)))]
        txt = self.clean(self.inline(wrap))
        return label, txt, level, aliases

    def heading(self, n):
        t, cl, i = n.tag, n.cls(), n.attrs.get('id')
        label, txt, level, aliases = self.heading_text(n)
        if i:
            self.emitted.add(i)
        for a in aliases:
            self.emitted.add(a)
        ids = ([i] if i else []) + aliases
        A = f', ids: ({"".join(q(x) + "," for x in ids)})' if ids else ''
        if t == 'h2':
            if i == 'table-of-contents':
                return ''
            return f'#parte({self.part}, {q(label or "")}, [{txt}]{A})'
        if t == 'h3':
            return f'#capitulo({q(label) if label else "none"}, [{txt}]{A})'
        if 'drsc-es-faq-q' in cl:
            a = next((c for c in n.children if isinstance(c, Node) and c.tag == 'a'), None)
            return f'#pregunta[{self.clean(self.inline(a)) if a else txt}]'
        if 'drsc-es-tabbed-item' in cl or 'drsc-es-tabbed-item-sub' in cl:
            sub = 'true' if 'drsc-es-tabbed-item-sub' in cl else 'false'
            lv = q(level) if level else 'none'
            return f'#ficha({int(t[1])}, [{txt}], {lv}, sub: {sub}{A})'
        estilo = 'pequeno' if 'drsc-es-header-small' in cl else ('linea' if 'drsc-es-border-line' in cl else 'normal')
        return f'#encabezado({int(t[1])}, [{txt}], estilo: {q(estilo)}{A})'

    def items(self, n):
        return [c for c in n.children if isinstance(c, Node) and c.tag == 'li']

    def item(self, li):
        parts = self.blocks(li)
        if li.attrs.get('id'):
            parts.insert(0, self.anchor(li.attrs['id']))
        return self.join(parts)

    def lista(self, n):
        cl = n.cls()
        lis = self.items(n)
        if 'drsc-es-play' in cl:
            rows = []
            for li in lis:
                sp = next((c for c in li.children if isinstance(c, Node) and c.tag == 'strong'), None)
                who = next((x[len('drsc-es-play-'):] for x in (sp.cls() if sp else ()) if x.startswith('drsc-es-play-')), 'dj')
                body = next((c for c in li.children if isinstance(c, Node) and c.tag == 'span'), None)
                rows.append(f'({q(who)}, [{self.clean(self.inline(sp)) if sp else ""}], [{self.clean(self.inline(body)) if body else ""}]),')
            return '#dialogo((' + ''.join(rows) + '))'
        if 'list-inline' in cl:
            return '#en-linea((' + ''.join(f'[{self.clean(self.inline(li))}],' for li in lis) + '))'
        content = ''.join(f'[{self.item(li)}],' for li in lis)
        if 'drsc-es-quick-reference' in cl or 'drsc-es-quick-reference-compact' in cl:
            return f'#refrapida(({content}))'
        if 'drsc-es-abilities-array' in cl:
            return f'#capacidades(({content}), compacta: {"true" if "drsc-es-abilities-compact" in cl else "false"})'
        if 'drsc-es-abilities-catalog' in cl:
            return f'#catalogo(({content}))'
        if 'list-unstyled' in cl or 'list-unstyled' in (n.parent.cls() if n.parent else set()):
            return f'#simple(({content}))'
        if n.tag == 'ol':
            return f'#numerada(({content}))'
        return f'#vinetas(({content}))'

    def tabla(self, n):
        rows, head, rojo = [], None, []
        for sec in n.children:
            if not isinstance(sec, Node):
                continue
            trs = [sec] if sec.tag == 'tr' else [c for c in sec.children if isinstance(c, Node) and c.tag == 'tr']
            for tr in trs:
                cells = [c for c in tr.children if isinstance(c, Node) and c.tag in ('td', 'th')]
                conv = []
                for c in cells:
                    s = self.clean(self.join(self.blocks(c)).replace('\n', ' #linebreak() '))
                    span = int(c.attrs.get('colspan', 1) or 1)
                    conv.append(f'table.cell(colspan: {span})[{s}]' if span > 1 else f'[{s}]')
                if sec.tag == 'thead' and head is None:
                    head = conv
                else:
                    if 'text-danger' in tr.cls():
                        rojo.append(len(rows))
                    rows.append(conv)
        ncols = max([sum(int(re.search(r'colspan: (\d+)', c).group(1)) if c.startswith('table.cell') else 1 for c in r) for r in ([head] if head else []) + rows] or [1])
        i = n.attrs.get('id')
        pre = self.anchor(i) + '\n' if i else ''
        h = '(' + ''.join(c + ',' for c in head) + ')' if head else 'none'
        body = '(' + ''.join('(' + ''.join(c + ',' for c in r) + '),' for r in rows) + ')'
        return pre + f'#tabla({ncols}, {h}, {body}, rojo: ({"".join(f"{x}," for x in rojo)}))'

    # ---------- document ----------
    def document(self, root):
        out = []
        parts = []
        def walk(n):
            for c in n.children:
                if isinstance(c, Node):
                    if c.tag == 'div' and re.fullmatch(r'part\d', c.attrs.get('id', '')):
                        parts.append(c)
                    else:
                        walk(c)
        walk(root)
        for part in parts:
            self.part = int(part.attrs['id'][4:])
            out.append(f'#fijar-parte({self.part})')
            kids = part.children
            if self.part == 0:
                # the web cover (title, versions) and the HTML TOC are replaced by the book's own
                start = next(k for k, c in enumerate(kids) if isinstance(c, Node) and c.tag == 'h2' and c.attrs.get('id') == 'el-sistema-cypher')
                kids = kids[start + 1:]
            wrap = Node('div'); wrap.children = kids
            out.extend(self.blocks(wrap))
        return '\n'.join(out) + '\n'


BLOCK = {'p', 'div', 'ul', 'ol', 'table', 'h2', 'h3', 'h4', 'h5', 'h6', 'dl', 'blockquote', 'hr'}


def has_block(n):
    return any(isinstance(c, Node) and (c.tag in BLOCK or has_block(c)) for c in n.children)


def find(n, pred):
    if isinstance(n, Node):
        if pred(n):
            return n
        for c in n.children:
            r = find(c, pred)
            if r is not None:
                return r
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--es', default='DRSC-ES.html')
    ap.add_argument('--out', default='book/build/contenido.typ')
    a = ap.parse_args()
    tree = Tree()
    tree.feed(Path(a.es).read_text(encoding='utf-8'))
    dry = Converter(known=set())
    dry.document(tree.root)
    conv = Converter(known=dry.emitted)
    out = conv.document(tree.root)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text('#import "../plantilla.typ": *\n' + out, encoding='utf-8')
    print(f'wrote {a.out}: {len(out):,} chars, {len(conv.emitted):,} labels')


if __name__ == '__main__':
    main()
