// Kurviak — Referencia rápida del Sistema Cypher (DRSC-ES)
// Typst source for the Spanish quick-reference. Build with ./build.sh
// Fonts live in assets/fonts (Teko, Orbitron, Open Sans).

#let blue = rgb("#175F81")
#let red = rgb("#BF2026")
#let thead = rgb("#CDDCE4")
#let rowc = rgb("#EEF3F6")
#let linec = rgb("#DDE6EC")
#let ink = rgb("#111111")
#let softline = rgb("#7FA9BE")

#set document(
  title: "Kurviak — Referencia rápida del Sistema Cypher",
  author: "Kurviak",
  keywords: ("Sistema Cypher", "referencia rápida", "DRSC-ES", "Kurviak"),
)

#set page(
  paper: "us-letter",
  margin: (top: 0.80in, bottom: 0.74in, left: 0.62in, right: 0.62in),
  header: context {
    align(right)[#text(font: "Orbitron", weight: 700, size: 9pt, tracking: 0.32em, fill: blue)[KUR-CSQR]]
    v(-0.04in)
    line(length: 100%, stroke: 1.4pt + blue)
  },
  header-ascent: 0.30in,
  footer: context {
    line(length: 100%, stroke: 1.4pt + blue)
    v(3pt)
    grid(
      columns: (1fr, auto),
      text(font: "Orbitron", weight: 500, size: 6.9pt, tracking: 0.06em, fill: blue)[KURVIAK — REFERENCIA RÁPIDA DEL SISTEMA CYPHER — 2026-11-14],
      text(font: "Orbitron", weight: 500, size: 6.9pt, fill: blue)[#counter(page).display()],
    )
  },
  footer-descent: 0.30in,
)

#set text(font: "Open Sans", size: 9.6pt, fill: ink, lang: "es")
#set par(leading: 0.60em)
#set enum(spacing: 0.5em, indent: 1.0em)
#set list(spacing: 0.4em)

// ---------- helpers ----------
#let h2(t) = block(above: 7pt, below: 2pt, text(font: "Teko", weight: 600, size: 15.5pt, fill: blue, t))
#let h2b(t) = block(above: 6pt, below: 2pt, text(font: "Teko", weight: 600, size: 14pt, fill: blue, t))

#let qr-table(header, rows, cols: none, aligns: none) = {
  let c = if cols == none { (1fr,) * header.len() } else { cols }
  let a = if aligns == none { (left,) * header.len() } else { aligns }
  let hcells = ()
  for (i, h) in header.enumerate() {
    hcells.push(table.cell(fill: thead, align(a.at(i), text(fill: blue, weight: 700, size: 8.6pt, h))))
  }
  let cells = (table.header(..hcells),)
  for (ri, r) in rows.enumerate() {
    let f = if calc.odd(ri) { rowc } else { white }
    for (ci, cell) in r.enumerate() {
      cells.push(table.cell(fill: f, align(a.at(ci), text(size: 8.6pt, cell))))
    }
  }
  table(columns: c, inset: (x: 4.5pt, y: 2.6pt), stroke: (bottom: 0.5pt + linec), ..cells)
}

// =========================== PAGE 1 ===========================
#align(center)[#text(font: "Orbitron", weight: 500, size: 13pt, tracking: 0.50em, fill: blue)[KURVIAK]]
#v(-4pt)
#align(center)[#text(font: "Teko", weight: 600, size: 33pt, fill: blue, tracking: 0.01em)[SISTEMA CYPHER: REFERENCIA RÁPIDA]]
#v(6pt)

#grid(
  columns: (53fr, 47fr),
  gutter: 0.24in,
  [
    #h2("CÓMO JUGAR")
    #enum(
      [Le dices al *DJ* qué *acción* quieres realizar y cómo planeas hacerlo. Incluye cualquier diálogo que quieras pronunciar mientras realizas tu acción.],
      [Muchas veces tus acciones son rutinarias —moverte unos pasos, hablar con otro personaje o girar el pomo de una puerta—: simplemente realizas la acción y tienes éxito automáticamente. Si hay posibilidad de fallo, el DJ te asigna una *tarea*, te dice cuál de tus *atributos* se pondrá a prueba —tu *Vigor*, *Velocidad* o *Intelecto*— y determina la *dificultad* en una escala del 1 (sencilla) al 10 (imposible).],
      [Tú y el DJ determináis si algo de tu PJ debe modificar la dificultad en uno o más grados. Estar entrenado en *habilidades* relevantes, tener *recursos* útiles y usar *Esfuerzo* alivian una tarea, reduciendo la dificultad. Tener una incapacidad o circunstancias externas adversas *obstaculizan* una tarea, aumentando la dificultad.],
      [Si alivias la dificultad hasta 0 (rutinaria), tienes éxito automáticamente. Si la tarea aún no es rutinaria, el DJ usa la dificultad modificada para determinar un *número objetivo*. El DJ no tiene que decirte el número objetivo, pero puede darte una pista.],
      [Tiras el dado —un d20—. Si el resultado iguala o supera el *número objetivo*, tienes éxito en la tarea.],
    )
    Eso es todo. Así se hace cualquier cosa: identificar un dispositivo desconocido, calmar a un borracho furioso, escalar un acantilado traicionero o combatir a un semidiós.
    #block(stroke: (left: 2.5pt + softline), inset: (left: 9pt, y: 1pt), above: 8pt)[
      #emph[El Sistema Cypher centra a los personajes y la narrativa. El DJ tiene la última palabra, pero tú —y tus compañeros de juego— dispones de mucho poder narrativo y libertad en la partida comparado con muchos otros juegos de rol de mesa: ¡aprovéchalo para sacar el máximo partido al juego!]
    ]
  ],
  [
    #block(width: 100%, stroke: 1.5pt + blue, inset: (x: 9pt, y: 8pt), radius: 1pt)[
      #h2b("PREPARACIÓN PARA JUGAR")
      *Hoja de personaje:* una hoja de papel para llevar el registro de la información sobre tu personaje jugador (PJ).

      #align(center)[#text(font: "Orbitron", weight: 700, size: 10.5pt, tracking: 0.10em, fill: blue)[SOY UN [DESCRIPTOR]\ [TIPO] QUE [RASGO]]]

      *Dados:* un dado de veinte caras (*d20*), un dado de seis caras (*d6*) y dos dados de diez caras (*d10*). Puedes compartir dados con los demás.

      #h2b("EL JUGADOR SIEMPRE TIRA")
      El DJ te asignará acciones y tareas, incluso cuando no hayas realizado una acción o no sea tu turno.
      #list(
        [Si atacas a un enemigo, tiras para ver si aciertas.],
        [Si un enemigo te ataca, tiras para ver si esquivas el golpe.],
        [Si saltas de un vehículo en movimiento, tiras para ver si lo consigues.],
        [Si un desprendimiento de rocas cae sobre ti, tiras para apartarte.],
      )
      La mayoría de las veces, las acciones que realizas cuando no es tu turno serán para *defenderte*.

      #v(8pt)
      #align(center)[#text(font: "Orbitron", weight: 700, size: 11pt, tracking: 0.16em, fill: blue)[DRSC-ES]]
      #v(4pt)
      #align(center)[#image("assets/qr.png", width: 1.55in)]
      #v(4pt)
      #align(center)[#text(size: 8.6pt, fill: blue)[https://jabelardo.github.io/drsc-es/DRSC-ES.html]]
    ]
  ],
)

#pagebreak()

// =========================== PAGE 2 ===========================
#set text(size: 9.2pt)
#block(above: 0pt, below: 7pt, text(font: "Teko", weight: 600, size: 30pt, fill: blue)[REFERENCIA RÁPIDA])

#grid(
  columns: (41fr, 59fr),
  gutter: 0.24in,
  [
    #block(width: 100%, stroke: 1.5pt + blue, inset: (x: 8pt, y: 6pt), radius: 1pt)[
      #h2b("¡INTENTA CUALQUIER COSA!")
      El DJ establece la dificultad. Si repites, usa 1 nivel de *Esfuerzo*.
    ]

    #h2("MODIFICAR LA DIFICULTAD")
    #qr-table(
      ([Habilidades (2 grados)], [Dificultad]),
      (
        ([Incapacidad], [+1]),
        ([Sin entrenamiento (predet.)], [—]),
        ([Competente], [−1]),
        ([Especialista], [−2]),
      ),
      cols: (1fr, auto),
      aligns: (left, right),
    )
    *Recursos (2 grados):* un objeto útil, ayuda o circunstancia favorable.

    *Esfuerzo (6 grados):* cuesta 3 puntos de *Reserva* + 2 puntos por cada nivel adicional.

    #h2("TIRADAS ESPECIALES")
    #qr-table(
      ([d20], [Efectos]),
      (
        ([1], [Intromisión del DJ, sin *PX*]),
        ([17], [+1 de daño]),
        ([18], [+2 de daño]),
        ([19], [Efecto menor o +3 de daño]),
        ([20], [Efecto mayor o +4 de daño, se devuelve la Reserva gastada]),
      ),
      cols: (0.5in, 1fr),
      aligns: (left, left),
    )

    #block(width: 100%, stroke: 1.5pt + blue, inset: (x: 8pt, y: 6pt), radius: 1pt, above: 6pt)[
      #h2b("PAGAR COSTES")
      Coste total de *Reserva*, resta la *Ventaja*.
    ]

    #block(width: 100%, stroke: 1.5pt + blue, inset: (x: 8pt, y: 6pt), radius: 1pt, above: 6pt)[
      #h2b("MOVIMIENTO")
      *Inmediato:* realiza una acción.\
      *Corto:* acción, tarea de Velocidad de dificultad 4 para otra acción.\
      *Largo:* tarea de Velocidad de dificultad 4.
    ]
  ],
  [
    #align(center)[#image("assets/dial.svg", width: 3.8in)]
    #align(center)[#text(size: 7.4pt, fill: blue)[*0* Rutinaria · *1* Sencilla · *2* Normal · *3* Ardua · *4* Difícil · *5* Desafiante · *6* Intimidante · #text(fill: red, weight: 700)[7 Abrumadora · 8 Heroica · 9 Legendaria · 10 Imposible]]]
    #v(2pt)
    #grid(
      columns: (1fr, 1fr),
      gutter: 0.20in,
      [
        #h2("GASTAR PX")
        #qr-table(
          ([PX], [Efecto]),
          (
            ([1 PX], [repetir tirada, evitar intromisión del DJ, crear intromisión de jugador]),
            ([2 PX], [habilidad o capacidad temporal]),
            ([3 PX], [trabajo, título, riqueza, hogar]),
            ([4 PX], [avance del personaje —aumenta Reserva, Esfuerzo, Ventaja o entrenamiento en una habilidad]),
          ),
          cols: (0.42in, 1fr),
          aligns: (left, left),
        )

        #h2("ALCANCE Y DISTANCIA")
        #qr-table(
          ([Distancia], [Alcance]),
          (
            ([Inmediato], [3 m [10 pies]]),
            ([Corto], [15 m [50 pies]]),
            ([Largo], [30 m [100 pies]]),
            ([Muy largo], [150 m [500 pies]]),
          ),
          cols: (1fr, 1fr),
          aligns: (left, left),
        )
      ],
      [
        #block(width: 100%, stroke: 1.5pt + blue, inset: (x: 8pt, y: 6pt), radius: 1pt, above: 0pt)[
          #h2b("CYPHERS")
          ¡Usa *Cyphers*, encontrarás más!
        ]

        #h2("COMBATE")
        #qr-table(
          ([Arma], [Daño], [Ataque]),
          (
            ([Ligera], [2], [aliviado]),
            ([Media], [4], [—]),
            ([Pesada], [6], [a dos manos]),
          ),
          cols: (1.1fr, 0.6fr, 1.2fr),
          aligns: (left, center, left),
        )
        *Daño por Esfuerzo:* +3 por nivel.

        #qr-table(
          ([Armadura], [Valor], [Coste Vel.]),
          (
            ([Ligera], [+1], [+2]),
            ([Media], [+2], [+3]),
            ([Pesada], [+3], [+4]),
          ),
          cols: (1.2fr, 0.6fr, 1.2fr),
          aligns: (left, center, center),
        )
      ],
    )
  ],
)
