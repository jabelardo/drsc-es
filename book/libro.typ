// Libro DRSC-ES: portada, índice y el contenido generado desde DRSC-ES.html (book/build/contenido.typ).
#import "plantilla.typ": *
#show: libro

// portada tipográfica (sin imágenes)
#page(columns: 1, header: none, footer: none, background: none, fill: colores.at(1))[
  #set text(fill: white)
  #v(1fr)
  #align(center)[
    #text(font: fuente-rotulos, size: 14pt, tracking: 0.5em)[DRSC-ES]
    #v(14pt)
    #text(font: fuente-titulos, weight: 600, size: 46pt, hyphenate: false)[DOCUMENTO DE REFERENCIA \ DEL SISTEMA CYPHER]
    #v(8pt)
    #text(font: fuente-titulos, weight: 500, size: 24pt)[EN ESPAÑOL]
    #v(26pt)
    #line(length: 40%, stroke: 1.5pt + white)
    #v(14pt)
    #text(font: fuente-rotulos, size: 10pt, tracking: 0.2em)[VERSIÓN DEL 2026-11-23 · CSRD DEL 2025-08-22]
  ]
  #v(1.4fr)
  #align(center, text(size: 9pt)[
    #strong[Traducción al español:] José Abelardo Gutiérrez Saturno \
    #strong[Corrección:] José Abelardo Gutiérrez Saturno, Parvus Domus \
    #strong[Maquetación:] José Abelardo Gutiérrez Saturno
  ])
]

// índice
#page(columns: 1, header: none)[
  #fijar-parte(0)
  #text(font: fuente-titulos, weight: 600, size: 32pt, fill: colores.at(0))[ÍNDICE]
  #v(6pt)
  #show outline.entry.where(level: 1): it => block(above: 1em, text(font: fuente-titulos, weight: 600, size: 14pt, it))
  #outline(title: none, depth: 2, indent: 1.2em)
]

#include "build/contenido.typ"
