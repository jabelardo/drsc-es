// Plantilla del libro DRSC-ES: maquetación inspirada en el Cypher System Rulebook (solo estilo y
// composición; sin imágenes). Fuentes libres (OFL): Teko (títulos), Alegreya Sans (texto),
// Aldrich (rótulos). Los colores de cada parte son los de DRSC-ES.html.

#let fuente-texto = "Alegreya Sans"
#let fuente-titulos = "Teko"
#let fuente-rotulos = "Aldrich"

#let colores = (rgb("#662255"), rgb("#224499"), rgb("#994422"), rgb("#776622"), rgb("#338844"), rgb("#444499"), rgb("#990000"))
#let oscuros = (rgb("#330033"), rgb("#003366"), rgb("#663300"), rgb("#554411"), rgb("#114422"), rgb("#222244"), rgb("#660000"))
#let tinta = rgb("#222222")
#let parte-n = state("parte-n", 0)
#let col() = colores.at(parte-n.get())
#let col-osc() = oscuros.at(parte-n.get())

#let anclas(ids) = for i in ids { [#metadata(none)#label(i)] }
#let fijar-parte(n) = parte-n.update(n)

// ---------- rótulos y títulos ----------
#let rotulo-versalitas(t, size: 10pt, fill: none) = context text(font: fuente-rotulos, size: size, tracking: 0.14em,
  fill: if fill == none { col() } else { fill }, upper(t))

#let rotulo(t) = context block(above: 0.9em, below: 0.4em, text(font: fuente-titulos, weight: 600, size: 11.5pt, fill: col(), upper(t)))

// ---------- página ----------
#let cabecera() = context {
  let p = here().page()
  let par = calc.even(p)
  let c = col()
  let caps = query(selector(heading.where(level: 2)).before(here()))
  // chapter opener pages carry no running title (the new title floats in after the header is laid out)
  let abre = query(heading.where(level: 2)).any(h => h.location().page() == p)
  let titulo = if abre { [] } else if caps.len() > 0 { caps.last().body } else { [] }
  set text(font: fuente-rotulos, size: 7.5pt, tracking: 0.16em, fill: c)
  block(width: 100%, inset: (bottom: 4pt), stroke: (bottom: 0.5pt + tinta.lighten(40%)))[
    #if par [
      #text(size: 11pt, tracking: 0.32em)[DRSC-ES] #h(1fr)
    ] else [
      #h(1fr) #upper(titulo)
    ]
  ]
}

#let pie() = context {
  let p = here().page()
  let c = col()
  let num = box(width: 22pt, height: 22pt, radius: 11pt, stroke: 1.6pt + c, fill: white,
    align(center + horizon, text(font: fuente-rotulos, size: 8.5pt, fill: c, str(counter(page).get().first()))))
  if calc.even(p) { align(left, num) } else { align(right, num) }
}

#let fondo() = context {
  let p = here().page()
  let c = col()
  // a coloured swoosh in the outer top corner, as in the rulebook's running header
  if calc.even(p) {
    place(top + left, polygon(fill: c, (0pt, 0pt), (120pt, 0pt), (70pt, 22pt), (0pt, 40pt)))
  } else {
    place(top + right, polygon(fill: c, (0pt, 0pt), (120pt, 0pt), (120pt, 40pt), (50pt, 22pt)))
  }
}

#let libro(cuerpo) = {
  set document(title: "Documento de Referencia del Sistema Cypher en Español", author: "José Abelardo Gutiérrez Saturno")
  set page(width: 603pt, height: 783pt, columns: 2,
    margin: (inside: 52pt, outside: 44pt, top: 62pt, bottom: 56pt),
    header: cabecera(), footer: pie(), background: fondo())
  set columns(gutter: 15pt)
  set text(font: fuente-texto, size: 9.8pt, fill: tinta, lang: "es", number-type: "old-style", hyphenate: true,
    costs: (widow: 100%, orphan: 100%))
  set par(justify: true, leading: 0.5em, spacing: 0.75em)
  set list(indent: 2pt, body-indent: 5pt, spacing: 0.5em)
  set enum(indent: 2pt, body-indent: 5pt, spacing: 0.5em)
  show link: it => context { if type(it.dest) == str { text(fill: col-osc(), it) } else { text(fill: col(), it) } }
  show strong: set text(weight: "bold")
  // the two characters the project fonts lack: the cyberware bolt (drawn) and the prescription sign
  show "⚡": context box(height: 0.75em, baseline: 0.05em, polygon(fill: col(),
    (0.32em, 0em), (0.62em, 0em), (0.45em, 0.3em), (0.66em, 0.3em), (0.18em, 0.75em), (0.33em, 0.4em), (0.12em, 0.4em)))
  show "℞": [R#sub[x]]
  show heading.where(level: 1): it => text(font: fuente-titulos, weight: 600, size: 60pt, hyphenate: false, upper(it.body))
  show heading.where(level: 2): it => context block(text(font: fuente-titulos, weight: 600, size: 38pt, fill: col(), hyphenate: false, upper(it.body)))
  show heading.where(level: 3): it => it.body
  show heading.where(level: 4): it => it.body
  show heading.where(level: 5): it => it.body
  cuerpo
}

// ---------- partes y capítulos ----------
#let parte(n, etiqueta, titulo, ids: ()) = {
  parte-n.update(n)
  pagebreak(to: "odd", weak: true)
  page(columns: 1, header: none, footer: none, background: none, fill: colores.at(n))[
    #anclas(ids)
    #set text(fill: white)
    #v(1fr)
    #align(center)[
      #if etiqueta != "" { text(font: fuente-rotulos, size: 16pt, tracking: 0.3em, upper(etiqueta)) }
      #v(10pt)
      #heading(level: 1, bookmarked: true, outlined: true, supplement: [#etiqueta])[#titulo]
    ]
    #v(1.2fr)
  ]
}

#let capitulo(etiqueta, titulo, ids: ()) = {
  pagebreak(weak: true)
  place(top, float: true, scope: "parent", clearance: 18pt, context {
    anclas(ids)
    let c = col()
    align(center)[
      #if etiqueta != none { text(font: fuente-rotulos, size: 13pt, tracking: 0.22em, fill: c, upper(etiqueta)) }
      #v(2pt)
      #heading(level: 2, supplement: if etiqueta != none [#etiqueta] else [])[#titulo]
      #v(4pt)
      #line(length: 100%, stroke: 2pt + c)
    ]
  })
}

#let encabezado(nivel, titulo, estilo: "normal", ids: ()) = context {
  let c = col()
  let (size, above) = if nivel == 4 { (16pt, 1.3em) } else if nivel == 5 { (13pt, 1.15em) } else { (11.5pt, 1em) }
  if estilo == "pequeno" { size = size - 1.5pt }
  let h = heading(level: calc.min(nivel - 1, 5), bookmarked: nivel <= 4, outlined: false)[#titulo]
  block(above: above, below: 0.45em, sticky: true, width: 100%,
    stroke: if estilo == "linea" { (bottom: 1.2pt + c) } else { none },
    inset: if estilo == "linea" { (bottom: 2pt) } else { 0pt })[
    #anclas(ids)
    #set par(justify: false)
    #text(font: fuente-titulos, weight: 600, size: size, fill: c, hyphenate: false, upper(h))
  ]
}

#let ficha(nivel, titulo, valor, sub: false, ids: ()) = context {
  let c = if sub { col-osc() } else { col() }
  block(above: 1.1em, below: 0.5em, sticky: true, width: 100%, fill: c, radius: 3pt,
    inset: (x: 6pt, top: 4pt, bottom: 2pt))[
    #anclas(ids)
    #set par(justify: false)
    #set text(font: fuente-titulos, weight: 600, size: if sub { 11.5pt } else { 13.5pt }, fill: white, hyphenate: false)
    #heading(level: calc.min(nivel - 1, 5), bookmarked: false, outlined: false)[#upper(titulo)]
    #if valor != none { h(1fr); upper(valor) }
  ]
}

#let pregunta(t) = context block(above: 1.1em, below: 0.5em, sticky: true, width: 100%, fill: col(), radius: 3pt,
  inset: (x: 6pt, top: 4pt, bottom: 3pt), par(justify: false, text(font: fuente-titulos, weight: 600, size: 12pt, fill: white, hyphenate: false, upper(t))))

// ---------- bloques ----------
#let recuadro(cuerpo) = context block(width: 100%, breakable: true, above: 1em, below: 1em,
  fill: col().lighten(90%), stroke: 1.2pt + col(), radius: 5pt, inset: (x: 8pt, y: 7pt), cuerpo)

#let lateral(cuerpo) = context block(width: 100%, breakable: true, above: 0.9em, below: 0.9em,
  stroke: (left: 2pt + col()), inset: (left: 7pt, y: 2pt),
  { set text(style: "italic", size: 9pt, fill: col-osc()); cuerpo })

#let refrapida(items) = block(width: 100%, above: 0.4em, below: 0.6em, {
  set text(size: 8.8pt, hyphenate: false)
  set par(justify: false, spacing: 0.35em)
  // two balanced columns (Typst columns would fill the first one before the second)
  let mitad = calc.ceil(items.len() / 2)
  let pila(xs) = stack(spacing: 0.4em, ..xs)
  grid(columns: (1fr, 1fr), column-gutter: 8pt, pila(items.slice(0, mitad)), pila(items.slice(mitad)))
})

#let capacidades(items, compacta: false) = context block(width: 100%, above: 0.5em, below: 0.7em, {
  set par(justify: false)
  let c = col()
  list(marker: box(baseline: -0.12em, circle(radius: 0.22em, fill: c)), spacing: 0.4em, ..items)
})

#let catalogo(items) = { for it in items { block(above: 0.55em, below: 0.55em, it) } }
#let simple(items) = { for it in items { block(above: 0.45em, below: 0.45em, it) } }
#let vinetas(items) = context list(marker: text(fill: col())[•], ..items)
#let numerada(items) = enum(..items)
#let en-linea(items) = items.join([ · ])
#let terminos(pares) = for (a, b) in pares { block(above: 0.6em, below: 0.3em)[#text(font: fuente-titulos, weight: 600, size: 11pt, upper(a))]; b }

#let tabla(n, cabeza, filas, rojo: ()) = context {
  let c = col()
  block(above: 0.8em, below: 0.9em, width: 100%, {
    set text(size: 8.8pt)
    set par(justify: false)
    table(columns: n, stroke: none, inset: (x: 4pt, y: 3pt),
      fill: (x, y) => if cabeza != none and y == 0 { c } else if calc.odd(y) { c.lighten(88%) } else { none },
      ..if cabeza != none { cabeza.map(h => text(fill: white, weight: "bold", h)) },
      ..filas.enumerate().map(((k, f)) => f.map(x => if k in rojo { text(fill: rgb("#b00000"), x) } else { x })).flatten())
  })
}

#let dialogo(filas) = {
  let colores-pj = (dj: rgb("#0b7a5c"), ori: rgb("#1864ab"), chert: rgb("#6741d9"), rena: rgb("#c2410c"))
  grid(columns: (auto, 1fr), column-gutter: 6pt, row-gutter: 0.55em,
    ..filas.map(((quien, nombre, texto)) => (align(right, text(weight: "bold", fill: colores-pj.at(quien, default: tinta), nombre)), texto)).flatten())
}

#let dial() = align(center, image("/quickref/assets/dial.svg", width: 80%))
#let video(titulo, url) = [Vídeo: #link(url)[#titulo]]
#let generador-web() = align(center, text(style: "italic")[El generador interactivo está en la #link("https://jabelardo.github.io/drsc-es/DRSC-ES.html#generador-de-frases-de-personaje")[versión web] de este documento.])
