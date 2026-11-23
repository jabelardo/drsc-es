// Kurviak — Hoja de personaje del Sistema Cypher (KUR-CSCS). Basada en la hoja no oficial de Old Gus (OG-CSCS).
// Compilar con sheets/build.sh (añade los campos rellenables).
#import "common.typ": *
#show: setup.with("KUR-CSCS", "Hoja de personaje")

#let L = 3.62in
#let R = 3.62in

// ---------- Cabecera ----------
#grid(columns: (1fr, 1.85in), column-gutter: 0.08in,
  panel(100%, 0.78in, inset: (x: 8pt, y: 6pt))[
    #grid(columns: (2.25in, 1fr, 2.25in), row-gutter: 5pt, align: (left, center + horizon, left),
      ufield("nombre", 2.25in, "Nombre"), sm("es un/una", size: 7.5pt), ufield("descriptor", 2.25in, "Descriptor"),
      ufield("tipo", 2.25in, "Tipo (aspecto)"), sm("que", size: 7.5pt), ufield("rasgo", 2.25in, "Rasgo"))
  ],
  brand("Hoja de personaje"))
#v(4pt)

#grid(columns: (L, R), column-gutter: 0.18in,
  // ---------- Columna izquierda ----------
  [
    #grid(columns: (0.72in, 0.72in, 1fr), column-gutter: 7pt,
      [#hd("Rango") #v(-6pt) #fieldbox("rango", 0.72in, 0.46in)],
      [#hd("Esfuerzo") #v(-6pt) #fieldbox("esfuerzo", 0.72in, 0.46in)],
      [#hd("Puntos de experiencia") #v(-6pt)
        #box(width: 100%, height: 0.46in, stroke: 1pt + ink, radius: 4pt,
          grid(columns: (1fr, 1fr), stroke: (x, y) => (left: if x > 0 { 0.8pt + ink } else { none }),
            [#align(center, sm("PX")) #area("px", 0.85in, 0.3in)],
            [#v(10pt) #area("px_notas", 0.85in, 0.3in)]))])
    #v(-2pt)
    #hd("Avance del personaje")
    #v(-6pt)
    #box(width: L, stroke: 1pt + ink, radius: 4pt, inset: (x: 4pt, y: 4pt),
      grid(columns: 5, column-gutter: 6pt,
        [#chk("avance_reservas") #sm("+4 a las Reservas")], [#chk("avance_ventaja") #sm("+1 a la Ventaja")],
        [#chk("avance_esfuerzo") #sm("+1 al Esfuerzo")], [#chk("avance_habilidad") #sm("Habilidad")],
        [#chk("avance_otras") #sm("Otras opciones")]))
    #v(-1pt)
    #hd("Atributos")
    #v(-6pt)
    #let stat(key, title) = box(width: 0.86in, height: 1.3in, stroke: 1pt + ink, radius: 5pt)[
      #pad(top: 3pt, align(center, if title == none { box(width: 0.7in, height: 11pt, stroke: (bottom: 0.8pt + ink), mark(key + "_nombre", "text", 0.7in, 11pt)) } else { hd(title, size: 11pt) }))
      #place(top + left, dy: 18pt, area(key + "_reserva", 0.86in, 0.36in))
      #place(top + left, dy: 0.56in, line(length: 0.86in, stroke: 0.8pt + ink))
      #place(top + left, dy: 0.56in, grid(columns: (0.43in, 0.43in), stroke: (x, y) => (left: if x > 0 { 0.8pt + ink } else { none }),
        [#pad(left: 3pt, top: 2pt, sm("Reserva", size: 5.8pt)) #area(key + "_reserva_max", 0.43in, 0.2in)],
        [#pad(left: 3pt, top: 2pt, sm("Ventaja", size: 5.8pt)) #area(key + "_ventaja", 0.43in, 0.2in)]))
      #place(top + left, dy: 0.96in, line(length: 0.86in, stroke: 0.8pt + ink))
      #place(top + center, dy: 0.98in, align(center)[#sm("Defensa", size: 6pt) #v(-5pt) #ipce-labels() #v(-5pt) #ipce(key + "_def")])
    ]
    #grid(columns: 4, column-gutter: 0.06in,
      stat("vigor", "Vigor"), stat("velocidad", "Velocidad"), stat("intelecto", "Intelecto"), stat("extra", none))
    #v(1pt)
    #legend
    #v(2pt)
    #grid(columns: (2.3in, 1fr), column-gutter: 8pt,
      [
        #grid(columns: (auto, 1fr, auto), align: horizon, column-gutter: 3pt,
          hd("Tiradas de recuperación", size: 11.5pt), align(right, box(sm("1d6 +", size: 8pt))), fieldbox("recuperacion_bonif", 0.42in, 0.2in))
        #v(-1pt)
        #box(width: 100%, stroke: 1pt + ink, radius: 4pt, inset: 3pt, tbl((0.98in, 1fr),
          (("una_accion", "Una acción"), ("diez_minutos", "Diez minutos"), ("una_hora", "Una hora"), ("diez_horas", "Diez horas")).map(r => (
            [#h(2pt)#chk("rec_" + r.at(0)) #sm(r.at(1))], area("rec_" + r.at(0) + "_notas", 1.2in, 14pt)))))
      ],
      [
        #hd("Registro de daño", size: 11.5pt)
        #v(-6pt)
        #box(width: 100%, stroke: 1pt + ink, radius: 4pt, inset: (x: 5pt, y: 4pt), stack(spacing: 4.6pt,
          ..(("ileso", "Ileso"), ("lesionado", "Lesionado"), ("incapacitado", "Incapacitado"), ("muerto", "Muerto")).map(r =>
            [#circ("dano_" + r.at(0)) #sm(r.at(1), size: 7pt)])))
      ])
    #v(-1pt)
    #hd("Capacidades especiales")
    #v(-6pt)
    #fieldbox("capacidades", L, 3.95in, kind: "multiline")
  ],
  // ---------- Columna derecha ----------
  [
    #theader((1.42in, 0.36in, 0.36in, 0.42in, 1fr),
      ([#hd("Armadura") #h(3pt) #box(baseline: 4pt, fieldbox("armadura", 0.55in, 0.2in))], sm("Coste"), sm("Atrib."), sm("Bonif."), sm("Detalles")))
    #v(-1pt)
    #panel(R, auto, inset: 3pt, tbl((1.42in, 0.36in, 0.36in, 0.42in, 1fr), range(3).map(i => (
      chkfield("arm_c" + str(i), "arm_n" + str(i), 1.42in),
      area("arm_coste" + str(i), 0.36in, 14pt), area("arm_atrib" + str(i), 0.36in, 14pt),
      area("arm_bonif" + str(i), 0.42in, 14pt), area("arm_det" + str(i), 0.9in, 14pt)))))
    #v(-1pt)
    #theader((1.78in, 0.36in, 0.36in, 0.48in, 1fr), (hd("Ataques"), sm("Coste"), sm("Atrib."), sm("Daño"), ipce-labels()))
    #v(-1pt)
    #panel(R, auto, inset: 3pt, tbl((1.78in, 0.36in, 0.36in, 0.48in, 1fr), range(6).map(i => (
      area("atq_n" + str(i), 1.78in, 14pt), area("atq_coste" + str(i), 0.36in, 14pt), area("atq_atrib" + str(i), 0.36in, 14pt),
      area("atq_dano" + str(i), 0.48in, 14pt), align(center, ipce("atq" + str(i)))))))
    #v(-1pt)
    #theader((2.5in, 0.48in, 1fr), (hd("Habilidades"), sm("Atrib."), ipce-labels()))
    #v(-1pt)
    #panel(R, auto, inset: 3pt, tbl((2.5in, 0.48in, 1fr), range(12).map(i => (
      area("hab_n" + str(i), 2.5in, 14pt), area("hab_atrib" + str(i), 0.48in, 14pt), align(center, ipce("hab" + str(i)))))))
    #v(1pt)
    #grid(columns: (auto, auto, 0.55in, auto, 0.55in, 1fr), align: horizon, column-gutter: 5pt,
      hd("Cyphers"), sm("Límite", size: 7.5pt), fieldbox("cyphers_limite", 0.55in, 0.2in), sm("+", size: 8pt),
      fieldbox("cyphers_limite_extra", 0.55in, 0.2in), box(width: 100%, height: 0.2in, stroke: (bottom: 0.8pt + ink), mark("cyphers_nota", "text", 0.9in, 0.2in)))
    #v(-1pt)
    #fieldbox("cyphers", R, 3.05in, kind: "multiline")
  ])

#pagebreak()

// ---------- Página 2 ----------
#page-two("", [
  #hd("Trasfondo y apariencia")
  #v(-6pt)
  #box(width: 3.62in, height: 2.0in, stroke: 1pt + ink, radius: 5pt,
    grid(columns: (1fr, 1.15in),
      area("trasfondo", 2.4in, 2.0in, kind: "multiline"),
      pad(3pt, box(width: 100%, height: 100%, stroke: 0.8pt + ink, radius: 2pt))))
])
