// Kurviak — Hoja de camarada del Sistema Cypher (KUR-CSSK). Basada en la hoja de compinche de Old Gus (OG-CSRD Sidekick Sheet).
// Compilar con sheets/build.sh (añade los campos rellenables).
#import "common.typ": *
#show: setup.with("KUR-CSSK", "Hoja de camarada")

#let L = 3.62in
#let R = 3.62in

// ---------- Cabecera ----------
#grid(columns: (1fr, 1.85in), column-gutter: 0.08in,
  panel(100%, 0.78in, inset: (x: 8pt, y: 6pt))[
    #grid(columns: (2.25in, 1fr, 1.25in, 0.95in), row-gutter: 5pt, column-gutter: 4pt, align: (left, center + horizon, left, left),
      ufield("nombre", 2.25in, "Nombre"), sm("es un/una", size: 7.5pt), ufield("naturaleza", 1.25in, "Naturaleza"), ufield("nicho", 0.95in, "Nicho"),
      ufield("tipo_criatura", 2.25in, "Tipo de criatura"), sm("para", size: 7.5pt), grid.cell(colspan: 2, ufield("pj_asociado", 2.24in, "PJ asociado")))
  ],
  brand("Hoja de camarada"))
#v(4pt)

#grid(columns: (L, R), column-gutter: 0.18in,
  [
    #grid(columns: (0.95in, 0.62in, 0.22in, 1fr), column-gutter: 5pt, align: bottom,
      [#hd("Nivel") #v(-6pt) #fieldbox("nivel", 0.95in, 0.46in)],
      [#sm("Recuperación", size: 8pt) #v(-2pt) #fieldbox("recuperacion", 0.62in, 0.46in)],
      align(center + horizon, pad(bottom: 0.16in, text(fill: soft, size: 13pt)[▶])),
      [#hd("Salud") #v(-6pt)
        #box(width: 100%, height: 0.46in, stroke: 1pt + ink, radius: 4pt,
          grid(columns: (1fr, 1fr), stroke: (x, y) => (left: if x > 0 { 0.8pt + ink } else { none }),
            area("salud", 0.7in, 0.46in), area("salud_max", 0.7in, 0.46in)))])
    #v(-1pt)
    #hd("Defensas")
    #v(-6pt)
    #box(width: L, height: 0.74in, stroke: 1pt + ink, radius: 5pt,
      grid(columns: (1fr, 1fr, 1fr), stroke: (x, y) => (left: if x > 0 { 0.8pt + ink } else { none }),
        ..(("vigor", "Vigor"), ("velocidad", "Velocidad"), ("intelecto", "Intelecto")).map(r => pad(top: 3pt, align(center)[
          #hd(r.at(1), size: 11pt) #v(-7pt) #ipce-labels() #v(-5pt) #ipce("def_" + r.at(0))
          #v(-3pt) #box(width: 0.9in, height: 9pt, stroke: (bottom: 0.6pt + ink), mark("def_" + r.at(0) + "_notas", "text", 0.9in, 9pt))]))))
    #v(1pt)
    #legend
    #v(1pt)
    #hd("Capacidades de camarada")
    #v(-6pt)
    #fieldbox("capacidades", L, 6.52in, kind: "multiline")
  ],
  [
    #theader((2.6in, 1fr),
      ([#hd("Armadura") #h(3pt) #box(baseline: 4pt, fieldbox("armadura", 0.55in, 0.2in))], sm("Bonif.")))
    #v(-1pt)
    #panel(R, auto, inset: 3pt, tbl((2.6in, 1fr), range(3).map(i => (
      chkfield("arm_c" + str(i), "arm_n" + str(i), 2.6in), area("arm_bonif" + str(i), 0.9in, 14pt)))))
    #v(-1pt)
    #theader((1.78in, 0.6in, 0.6in, 1fr), (hd("Ataques"), sm("Coste"), sm("Daño"), ipce-labels()))
    #v(-1pt)
    #panel(R, auto, inset: 3pt, tbl((1.78in, 0.6in, 0.6in, 1fr), range(6).map(i => (
      area("atq_n" + str(i), 1.78in, 14pt), area("atq_coste" + str(i), 0.6in, 14pt),
      area("atq_dano" + str(i), 0.6in, 14pt), align(center, ipce("atq" + str(i)))))))
    #v(-1pt)
    #theader((2.98in, 1fr), (hd("Habilidades"), ipce-labels()))
    #v(-1pt)
    #panel(R, auto, inset: 3pt, tbl((2.98in, 1fr), range(12).map(i => (
      area("hab_n" + str(i), 2.98in, 14pt), align(center, ipce("hab" + str(i)))))))
    #v(1pt)
    #hd("Apariencia")
    #v(-6pt)
    #fieldbox("apariencia", R, 3.42in, kind: "multiline")
  ])

#pagebreak()

#page-two("", [
  #v(13.6pt)
  #fieldbox("notas_superior", 3.62in, 2.0in, kind: "multiline")
])
