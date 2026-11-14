# Plan for Full Parity: DRSC-ES → OG-CSRD

Status: draft for execution
Scope: bring the Spanish `DRSC-ES.html` to full content and structural parity with the
current Old Gus' Cypher System Reference Document (OG-CSRD).

Reference version analysed: OG-CSRD v2.11a (2026-08-14), covering CSRD 2015–2025
(CSRD text of 2025-08-22). Current ES source is the CSRD of 2023-04-18 plus selected
supplements (Godforsaken, The Stars Are Fire, We Are All Mad Here, Claim the Sky,
Stay Alive!, Cypher Shorts).

---

## 1. Definition of done

Full parity means:

1. Every section present in OG-CSRD has an equivalent section in DRSC-ES, with
   equivalent rules content (not necessarily identical wording).
2. All new material is fully translated, not machine-pasted, using the existing
   Spanish terminology and the `[English]` bilingual label convention.
3. Every new heading has an id and a permalink anchor; every internal link resolves.
4. TOC, navbar dropdowns, quick-reference boxes, part colours and theme styling
   cover all new/expanded chapters.
5. The Index, FAQ, What's in the Book and other OG editorial/tool sections exist
   in Spanish.
6. No ES-only content is lost (magic-rules module, expanded sci-fi/fairy-tale,
   Cypherpunk/Dark Sun extras are preserved).
7. QA passes: 0 missing internal anchors, no new duplicate ids, valid HTML
   structure, light/dark render with no console errors.

---

## 2. Source strategy

- **Primary source of truth: OG-CSRD (English).** Translate from the current
  OG-CSRD so structure, cross-links, quick references and optional rules match by
  construction.
- **Verification sources:** official CSRD (2025-08-22), Cypher System Rulebook
  (2019/2024), and the supplement PDFs (Godforsaken, The Stars Are Fire, We Are All
  Mad Here, Claim the Sky, Stay Alive!, Cypher Shorts, It's Only Magic, Neon Rain,
  High Noon at Midnight, Rust and Redemption, Cypher System Bestiary).
- **Terminology:** reuse the existing DRSC-ES glossary; keep English names in
  `[brackets]` exactly as the current document does.
- **Editorial policy:** full parity includes OG editorial content (foreword, editor
  notes, page citations, "Related Sections", Index, FAQ, What's in the Book,
  Character Sentence Generator, PDFs/Player's Guide links). Where OG makes an
  editorial ruling that differs from the official CSRD, preserve the official rules
  wording and mark the OG addition as such (a Spanish equivalent of the OG badge).

---

## 3. Current gap summary

Approximate word counts (EN source compared with ES). Spanish typically expands
10–20% for the same text, so the Spanish output volume will be larger than the EN
figures below.

| EN chapter | EN words | ES counterpart | ES words | Status |
|---|---:|---|---:|---|
| Ch1 Foreword | 538 | — | 0 | missing |
| Ch2 Open License | 81 | Licencia (under El Sistema Cypher) | — | present |
| Ch3 How to Play | 3,311 | Cómo jugar | 3,477 | parity |
| Ch4 Creating Your Character | 6,623 | Creación de personajes | 4,382 | partial |
| Ch5 Type | 10,471 | Tipos de personaje | 9,880 | partial |
| Ch6 Flavor | 2,876 | Aspectos de personaje | 1,255 | partial |
| Ch7 Descriptor | 17,546 | Descriptores de personaje | 13,818 | partial |
| Ch8 Focus | 39,176 | Rasgos de personaje | 23,279 | partial |
| Ch9 Abilities | 112,889 | Capacidades + Listado | 79,134 | partial |
| Ch10 Equipment | 4,276 | Equipo | 6,207 | ES ahead |
| Ch11 Rules of the Game | 24,482 | Reglas del juego | 21,729 | partial |
| Ch11-A Followers & Factions | 13,482 | Seguidores | small | partial |
| Ch12 Experience Points | 13,229 | Puntos de experiencia | 9,806 | partial |
| Ch13 Fantasy | 32,130 | Fantasía | 5,064 | partial |
| Ch14 Modern | 5,838 | Moderno | 1,054 | partial |
| Ch14-A Modern Magic | 16,775 | — | 0 | missing |
| Ch14-B Cyberpunk | 35,119 | — | 0 | missing |
| Ch15 Science Fiction | 29,399 | Ciencia ficción | 46,011 | ES ahead |
| Ch16 Horror | 18,340 | Horror | 19,123 | parity/ES ahead |
| Ch17 Romance | 1,528 | Romance | 1,438 | parity |
| Ch18 Superheroes | 10,873 | Superhéroes | 10,050 | near parity |
| Ch19 Post-Apocalyptic | 21,766 | Post-apocalíptico | 2,430 | partial |
| Ch20 Fairy Tale | 25,805 | Cuentos de hadas | 37,844 | ES ahead |
| Ch21 Historical | 1,097 | Histórico | 1,115 | parity |
| Ch21-A Weird West | 26,993 | — | 0 | missing |
| Ch22 Creatures | 62,049 | Criaturas | 43,278 | partial |
| Ch23 NPCs | 31,083 | PNJs | 4,730 | partial |
| Ch24 Cyphers | 16,510 | Cyphers | 17,531 | parity/ES ahead |
| Ch25 Running the Cypher System | 24,737 | Dirigir el Sistema Cypher | 16,174 | partial |
| Cypher Shorts | 1,927 | Cypher cortos | 1,751 | parity |
| Trapped in Flames | 1,893 | Atrapado en llamas | 1,946 | parity |
| FAQ | 3,875 | — | 0 | missing |
| Index | 1,015 | — | 0 | missing |
| What's in the Book | 5,886 | — | 0 | missing |

Net gap ≈ 227k EN words; gross EN-only ≈ 270k. Estimated Spanish output to reach
parity: **~300k+ words**.

Entry-level gaps (approximate):

| Item | EN | ES | Missing |
|---|---:|---:|---:|
| Descriptors | ~106 | 50 (+genre species) | ~56 |
| Foci | ~149 | ~105 | ~44 |
| Abilities | ~1,500 | ~1,129 | ~370+ |
| Optional rules | ~55–68 | ~19 | ~40+ |
| Flavors | 10 | 5 | 5 |
| Cyphers | ~188 | ~198 | parity |
| Unique creature/NPC stat blocks | ~236 | creature ch. 89 + NPC ch. 16 | NPCs mostly missing |
| Quick-reference boxes | ~70 | 38 | rest follow new sections |

Missing supplement sources: It's Only Magic (Modern Magic), Neon Rain (Cyberpunk),
High Noon at Midnight (Weird West), Rust and Redemption (post-apocalyptic expansion),
Cypher System Rulebook 2024 errata, Cypher System Bestiary.

---

## 4. Target structure

Adopt the OG-CSRD five-part structure and English chapter order, and preserve the
ES-only material in an appendix so nothing is lost.

- Part 0 / front: Prólogo (Foreword), Licencia, Cómo jugar.
- Part 1 Characters: Creación, Tipos, Aspectos, Descriptores, Rasgos, Capacidades,
  Equipo.
- Part 2 Rules: Reglas del juego, Seguidores y facciones, Puntos de experiencia.
- Part 3 Genres: Fantasía, Moderno, Magia moderna, Cyberpunk, Ciencia ficción,
  Horror, Romance, Superhéroes, Post-apocalíptico, Cuentos de hadas, Histórico,
  Oeste extraño.
- Part 4 Game Mastering: Criaturas, PNJs, Cyphers, Dirigir el Sistema Cypher.
- Part 5 Back matter: Cypher cortos, Atrapado en llamas, FAQ, Índice,
  Qué hay en el libro.
- Appendix (ES-only, preserved): Módulo de reglas mágicas, Extras
  (Cypherpunk / Dark Sun PDFs).

Renumber chapters to match the final order and update the TOC and navbar.

---

## 5. Work packages

### WP0 — Setup (0.5–1 day)
- [ ] Record the locked source version in the document header.
- [ ] Create `GLOSARIO.md` (EN→ES term map) and `TRADUCCION-PROGRESO.md`
      (per-section status).
- [ ] Add QA scripts: anchor target check, duplicate-id check, HTML structure check,
      headless render (light/dark).
- [ ] Confirm appendix handling for ES-only content.

### WP1 — Core rules and character options (~90–100k EN words)
- [ ] Ch4: optional rules (skills from backgrounds, switching options, effort after
      rolling, paying with other pools), creation checklist, sentence generator.
- [ ] Ch5: additional/cyberpunk/fairy-tale types and type options.
- [ ] Ch6: 5 missing flavors (Roles, Charms & Figments, Cozy Magic, Divination,
      Protection) + simplified/personalized flavor + Additional Flavors.
- [ ] Ch7: genre/species descriptors (cyberpunk, weird west, modern magic, etc.).
- [ ] Ch8: ~44 missing foci, focus categories, customizing/creating foci.
- [ ] Ch9: ~370+ abilities (core updates, cantrips, mutations, paranormal vices,
      genre abilities, errata).
- [ ] Ch11: ~40 missing optional rules (damage dice, ultimate damage, object
      level/health/armor, drowning, acting while under attack, etc.).
- [ ] Ch11-A: Seguidores y facciones (Followers, Familiars, Sidekicks, Covens).
- [ ] Ch12: split XP, tier 0, slower advancement, beyond tier 6, XP advance,
      equal advancement, optional advancements.
- [ ] Add quick-reference boxes and anchors for every new section.
- Acceptance: all WP1 sections translated, linked, quick-referenced; anchor/QA clean.

### WP2 — Genre parity (~130k EN words)
- [ ] 2a — complete existing genres:
      - Fantasy: equipment by price, Dungeons/Castles/Traps, fantasy cyphers,
        artifacts, creatures, character options/foci.
      - Modern: character options, modern equipment, vehicles, creatures.
      - Post-apocalyptic: character options, equipment, optional rules, mutations,
        cyphers, artifacts, creatures.
- [ ] 2b — translate new chapters in full:
      - Magia moderna (It's Only Magic): character options, equipment, crafting
        ingredients, cyphers, artifacts, creatures/NPCs.
      - Cyberpunk (Neon Rain): cybernetics, types, descriptors, foci, dystopian
        society, drugs, technology, SHITS, hacking, netrunning, rules, cyphers,
        GM intrusions, creatures.
      - Oeste extraño (High Noon at Midnight): character options, currency,
        equipment, poker/hands of fate/deck as d20, showdown, curses, survival,
        tall tales, paranormal vices, threats/hazards, cyphers, artifacts, creatures.
- [ ] Add TOC/nav entries, part colours, quick-reference boxes for each new chapter.
- Acceptance: genre chapters at parity; ES-ahead genres left unchanged.

### WP3 — Bestiary and NPCs (~45k EN words)
- [ ] Creatures: add missing bestiary entries and supplement creatures.
- [ ] NPCs: full roster (aristocrat, assassin, bard, witch, etc.) + supervillains.
- [ ] Normalise creature/NPC ids and stat-block markup; add quick references.
- Acceptance: creature/NPC counts at parity; no missing referenced creatures.

### WP4 — Back matter and tools (~15–20k EN words)
- [ ] FAQ (Troubleshooting).
- [ ] Index (Spanish equivalent of the OG-CSRD index).
- [ ] Qué hay en el libro (product index).
- [ ] Character Sentence Generator (Spanish).
- [ ] Editor notes, "Related Sections", page citations (decide whether to keep
      OG page numbers or map to Spanish/CSRD pages).
- Acceptance: all back-matter sections present and linked from TOC/nav.

### WP5 — Structural integration
- [ ] Renumber/reorder to the target structure in §4.
- [ ] Update TOC and both navbar dropdowns.
- [ ] Extend part-colour theming and quick-reference styling to new content.
- [ ] Fix the 134 pre-existing duplicate ids and normalise new ids.
- [ ] Preserve ES-only appendix material.
- Acceptance: navigation complete; no orphan sections; anchors coherent.

### WP6 — QA and release
- [ ] Run anchor/duplicate/structure checks (expect 0 missing anchors, no new dupes).
- [ ] Headless render in light and dark; confirm no console errors.
- [ ] Link sweep and cross-reference audit.
- [ ] Proofread pass against the glossary.
- [ ] Bump the version line and the `?v=` cache-bust params for CSS/JS.
- Acceptance: all QA checks green; parity checklist signed off.

---

## 6. Translation and HTML conventions

- Use the `drsc-es-*` classes and existing structures (headings h2=part, h3=chapter,
  h4/h5/h6=sections; `drsc-es-tabbed-item` for stat blocks; `drsc-es-quick-reference`
  for quick refs; `drsc-es-sidebar`/`alert` for boxes).
- Each heading gets an id and a permalink anchor:
  `<a class="drsc-es-header-anchor" href="#id" title="Permalink" aria-hidden="true"></a>`.
- Keep `Nombre en español [English Name]` for game elements.
- New chapters get a part colour in `css/drsc-es.css` if a new part is introduced.
- New sections get a "Referencia rápida" box listing their immediate subheadings.
- Use relative internal links (`#id`) inside the page; external links only for
  genuine external resources.
- Do not introduce inline styles; extend `css/drsc-es.css`.

---

## 7. Terminology governance

- Maintain `GLOSARIO.md` with one canonical Spanish term per English term.
- Follow existing choices from the translation notes (e.g., Cypher=Cypher,
  ease=aliviar, hinder=obstaculizar, round=ronda, trained=competente,
  specialized=especialista).
- Flag conflicts early; do not silently vary terms across chapters.

---

## 8. QA and verification

Automated checks to run after each work package (scripts already prototyped):

1. Internal anchors: every `href="#x"` resolves to an `id="x"`.
2. Duplicate ids: no new duplicates; drive the pre-existing 134 to zero.
3. HTML structure: balanced tags, no unclosed containers.
4. Render: load in headless Chromium (light and dark), assert no page errors, spot
   check tables, sidebars, quick refs, tabbed items and dropdowns.
5. Coverage: compare section counts against OG-CSRD per chapter.

---

## 9. Milestones and sequencing

| Milestone | Content | Depends on |
|---|---|---|
| M1 | Core character options (Ch4–Ch9) | WP0 |
| M2 | Rules, followers, XP (Ch11–Ch12) | WP0 |
| M3 | Existing genres completed | M1 |
| M4 | New genres (Magic, Cyberpunk, Weird West) | M1, M2 |
| M5 | Bestiary and NPCs | M1 |
| M6 | Back matter and tools | M2 |
| M7 | Structural integration + full QA | M1–M6 |

Recommended order: WP0 → WP1 → WP2a → WP2b → WP3 → WP4 → WP5 → WP6, with WP5
integrated incrementally per chapter to keep anchors and navigation consistent.

---

## 10. Effort estimate

- Translation volume: ~270k EN source words → ~300k+ Spanish words.
- Throughput: ~1,500–2,500 words/day for prose; slower for stat blocks and
  link-heavy lists.
- Estimate: **~120–180 person-days** for one translator/editor, parallelisable by
  chapter or source book.
- Calendar: roughly 7–10 months at ~20 working days/month for one person; faster
  with a small team split by genre/source.

---

## 11. Risks and mitigations

| Risk | Mitigation |
|---|---|
| OG editorial rulings diverge from official CSRD | Keep official rules wording; mark OG additions explicitly |
| Terminology drift across hundreds of entries | `GLOSARIO.md` + review gate per milestone |
| Duplicate/broken ids while adding hundreds of entries | Automated id/anchor checks each WP; fix pre-existing dupes |
| Losing ES-only content during restructure | Keep explicit appendix; diff against baseline after restructure |
| File size/performance growth (~4 MB → 6–7 MB) | Monitor load time; consider section splitting if needed |
| Scope creep (OG tools/randomizer/tooltips) | Use the definition of done; treat tools as WP4 optional items |

---

## 12. Immediate next actions

1. Create `GLOSARIO.md` and `TRADUCCION-PROGRESO.md`.
2. Add the QA scripts to the repo (read-only checks).
3. Start WP1 with Flavor and Focus (small, self-contained, high value), then Abilities.
4. After each chapter, update TOC/nav/quick refs and run QA before moving on.
