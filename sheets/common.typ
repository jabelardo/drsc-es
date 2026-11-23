// Kurviak — piezas comunes de las hojas de personaje del Sistema Cypher (DRSC-ES).
// Cada zona rellenable deja un <fld> con su posición; sheets/add_fields.py los convierte en campos de formulario.

#let blue = rgb("#175F81")
#let ink = rgb("#1A1A1A")
#let rowc = rgb("#EEF3F6")
#let soft = rgb("#7FA9BE")

#let setup(code, title, body) = {
  set document(title: "Kurviak — " + title, author: "Kurviak",
    keywords: ("Sistema Cypher", "hoja de personaje", "DRSC-ES", "Kurviak"))
  set page(paper: "us-letter", margin: (top: 0.42in, bottom: 0.46in, x: 0.42in),
    footer: context align(right, text(font: "Orbitron", size: 5.6pt, tracking: 0.08em, fill: blue)[
      #code — KURVIAK — #upper(title) DEL SISTEMA CYPHER — 2026-11-23]),
    footer-descent: 0.16in)
  set text(font: "Open Sans", size: 7pt, fill: ink, lang: "es")
  set par(leading: 0.4em)
  body
}

// Etiquetas
#let hd(t, size: 12.5pt) = text(font: "Teko", weight: 600, size: size, fill: blue, upper(t))
#let sm(t, size: 6.6pt, fill: ink) = text(font: "Teko", weight: 500, size: size, fill: fill, upper(t))

// Marca de campo
#let mark(name, kind, w, h) = context {
  let p = here().position()
  [#metadata((name: name, kind: kind, page: p.page, x: p.x.pt(), y: p.y.pt(), w: w.pt(), h: h.pt()))<fld>]
}
#let area(name, w, h, kind: "text") = box(width: w, height: h, mark(name, kind, w, h))

// Campo subrayado con etiqueta debajo
#let ufield(name, w, label, h: 13pt) = stack(dir: ttb, spacing: 1.6pt,
  box(width: w, height: h, stroke: (bottom: 0.8pt + ink), mark(name, "text", w, h)),
  sm(label, size: 6.4pt))

// Casilla, círculo
#let chk(name, s: 7.5pt) = box(width: s, height: s, stroke: 0.8pt + ink, baseline: 0.5pt, mark(name, "check", s, s))
#let circ(name, s: 8.4pt) = box(width: s, height: s, baseline: 1.5pt,
  [#place(circle(radius: s / 2, stroke: 0.8pt + ink))#mark(name, "circle", s, s)])

// I P C E
#let ipce-labels(gap: 1.2pt) = grid(columns: 4, column-gutter: gap,
  ..("I", "P", "C", "E").map(l => box(width: 8.4pt, align(center, sm(l, size: 6pt)))))
#let ipce(prefix, gap: 1.2pt) = grid(columns: 4, column-gutter: gap,
  ..("i", "p", "c", "e").map(k => circ(prefix + "_" + k)))

// Recuadros
#let panel(w, h, body, inset: 4pt) = block(width: w, height: h, stroke: 1pt + ink, radius: 5pt, inset: inset, body)
#let fieldbox(name, w, h, kind: "text") = box(width: w, height: h, stroke: 1pt + ink, radius: 4pt,
  mark(name, kind, w, h))

// Fila de tabla: celdas (ancho, contenido); fondo alterno
#let trow(i, cells, h: 13pt) = grid(columns: cells.map(c => c.at(0)), rows: h,
  fill: if calc.odd(i) { rowc } else { white },
  stroke: (x, y) => (left: if x > 0 { 0.6pt + ink } else { none }, bottom: 0.6pt + ink),
  ..cells.map(c => align(horizon, c.at(1))))

#let legend = sm("I = Incapacidad   P = Practicado   C = Competente   E = Especialista", size: 6.2pt)

// Fila de etiquetas alineada con las columnas de una tabla (cols: anchos; cells: contenidos)
#let theader(cols, cells) = pad(x: 4pt, grid(columns: cols, align: (x, y) => if x == 0 { left + bottom } else { center + bottom }, ..cells))

// Tabla de una sola rejilla: filas alternas y líneas interiores coherentes
#let tbl(cols, rows, h: 14pt) = grid(columns: cols, rows: h,
  fill: (x, y) => if calc.odd(y) { rowc } else { white },
  stroke: (x, y) => (left: if x > 0 { 0.6pt + ink } else { none }, top: if y > 0 { 0.6pt + ink } else { none }),
  align: horizon, ..rows.flatten())
// Casilla + campo en la misma celda
#let chkfield(cname, fname, w, h: 14pt) = grid(columns: (11pt, 1fr), align: horizon, align(center, chk(cname)), area(fname, w - 11pt, h))

// Bloque de créditos con QR y licencia (página 2)
#let credits(w) = block(width: w)[
  #grid(columns: (1fr, 1.05in), column-gutter: 8pt,
    align(center)[
      #stack(spacing: 4pt,
        text(font: "Orbitron", weight: 500, size: 8pt, tracking: 0.4em, fill: blue)[KURVIAK],
        text(font: "Teko", weight: 600, size: 24pt, fill: blue, top-edge: "cap-height", bottom-edge: "baseline")[DRSC-ES],
        text(font: "Teko", weight: 500, size: 12pt, fill: blue, top-edge: "cap-height", bottom-edge: "baseline")[DOCUMENTO DE REFERENCIA],
        text(font: "Teko", weight: 500, size: 12pt, fill: blue, top-edge: "cap-height", bottom-edge: "baseline")[DEL SISTEMA CYPHER],
        text(size: 6.4pt, fill: blue)[https://jabelardo.github.io/drsc-es/DRSC-ES.html])
    ],
    image("../quickref/assets/qr.png", width: 1.05in))
  #v(2pt)
  #text(size: 5.6pt)[Este producto es una producción independiente y no está afiliado a Monte Cook Games, LLC. Se publica bajo la Licencia Abierta del Sistema Cypher (Cypher System Open License), que se encuentra en http://csol.montecookgames.com.]
  #v(1pt)
  #text(size: 5.6pt)[El Sistema Cypher (CYPHER SYSTEM) y su logotipo son marcas registradas de Monte Cook Games, LLC en EE. UU. y otros países. Todos los personajes y nombres de personajes de Monte Cook Games, así como sus aspectos distintivos, son marcas registradas de Monte Cook Games, LLC.]
]

// Marca de la hoja (arriba a la derecha)
#let brand(title) = align(right, stack(spacing: 3pt,
  text(font: "Orbitron", weight: 500, size: 8pt, tracking: 0.42em, fill: blue)[KURVIAK],
  text(font: "Teko", weight: 600, size: 20pt, fill: blue, top-edge: "cap-height", bottom-edge: "baseline")[SISTEMA~CYPHER],
  text(font: "Teko", weight: 500, size: 14pt, fill: blue, top-edge: "cap-height", bottom-edge: "baseline")[#upper(title)]))

// Página 2 común: dos recuadros a la izquierda; a la derecha un recuadro superior, dos tablas y los créditos
#let page-two(prefix, top-right) = {
  let L = 3.62in
  let R = 3.62in
  grid(columns: (L, R), column-gutter: 0.18in,
    [
      #ufield(prefix + "p2_titulo1", L - 0.2in, "", h: 12pt)
      #v(1pt)
      #fieldbox(prefix + "p2_texto1", L, 4.92in, kind: "multiline")
      #v(8pt)
      #ufield(prefix + "p2_titulo2", L - 0.2in, "", h: 12pt)
      #v(1pt)
      #fieldbox(prefix + "p2_texto2", L, 4.22in, kind: "multiline")
    ],
    [
      #top-right
      #v(6pt)
      #theader((1.76in, 1.36in, 1fr), (ufield(prefix + "t1_h1", 1.7in, "", h: 10pt), ufield(prefix + "t1_h2", 1.3in, "", h: 10pt), ufield(prefix + "t1_h3", 0.36in, "", h: 10pt)))
      #panel(R, auto, inset: 3pt, tbl((1.76in, 1.36in, 1fr), range(12).map(i => (
        chkfield(prefix + "t1_c" + str(i), prefix + "t1_a" + str(i), 1.76in),
        area(prefix + "t1_b" + str(i), 1.36in, 14pt), area(prefix + "t1_n" + str(i), 0.4in, 14pt)))))
      #v(6pt)
      #theader((1.32in, 0.38in, 1.32in, 1fr), (ufield(prefix + "t2_h0", 1.26in, "", h: 10pt), ufield(prefix + "t2_h1", 0.32in, "", h: 10pt), ufield(prefix + "t2_h2", 1.26in, "", h: 10pt), ufield(prefix + "t2_h3", 0.32in, "", h: 10pt)))
      #panel(R, auto, inset: 3pt, tbl((1.32in, 0.38in, 1.32in, 1fr), range(5).map(i => (
        area(prefix + "t2_a" + str(i), 1.32in, 14pt), area(prefix + "t2_x" + str(i), 0.38in, 14pt),
        area(prefix + "t2_b" + str(i), 1.32in, 14pt), area(prefix + "t2_y" + str(i), 0.38in, 14pt)))))
      #v(10pt)
      #credits(R)
    ])
}
