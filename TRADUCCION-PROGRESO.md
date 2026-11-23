# Progreso de la traducción

Per-chapter status of DRSC-ES against OG-CSRD v2.11a (2026-08-14). The work packages
(WP) are defined in `PLAN-FULL-PARITY.md` §5.

- **Covered books**: Cypher System Rulebook, Godforsaken, The Stars Are Fire, We Are All
  Mad Here, Claim the Sky, Stay Alive!, Cypher Shorts. Their content is in DRSC-ES unless
  a gap is listed.
- **Supplements to translate**: It's Only Magic (IOM, WP3), Neon Rain (NR, WP4), High
  Noon at Midnight (HNAM, WP5), Rust and Redemption (RR, WP6).
- **OG editorial**: OG-CSRD additions that are not CSRD text (WP7).
- Word counts are English words in OG-CSRD (k = thousand).
- Refresh the numbers with `python3 tools/parity/audit.py`.
- When you start or finish an item, update its row: Status is *to do*, *in progress* or
  *done*, with the date and branch.

## Work packages

| WP | Scope | Status |
|---|---|---|
| WP0 | Setup: source version, glossary, this file, QA scripts, audit | in progress (2026-11-22, `wp0-setup`) |
| WP1 | Reorganise existing Spanish content to the OG structure | done (2026-11-22, `wp1-fantasy-relocation`, not merged yet) |
| WP2 | Gaps inside covered books, CSRD 2025 errata | done (2026-11-22, `wp2-gaps`, not merged yet): range/distance terminology, Heartwood, Moonbeam and Question Past Self; the CSRD 2025 has no errata to existing text; *Escudo deflector* kept |
| WP3 | It's Only Magic (~48k) | done (2026-11-22, merged in #3): abilities, cantrips, flavors and foci; fantasy roles; Magia moderna chapter (Cap. 12-A); 13 creatures and 4 NPCs; Familiars and Covens; Reviving Artifacts; crafting additions |
| WP4 | Neon Rain (~42k) | done (2026-11-23, merged in #4): 52 abilities, 9 foci, 5 descriptors, Cap. 12-B Ciberpunk, Ch11 optional rules, Splitting XP, Romance addition, linking pass; 5 links wait for WP7 sections |
| WP5 | High Noon at Midnight (~38k) | done (2026-11-23, merged in #5): 76 abilities, 7 foci, 9 descriptors, Cap. 19-A Oeste extraño, 11 creatures, 2 NPCs, linking pass; 5 links wait for WP6/WP7 sections |
| WP6 | Rust and Redemption (~36k) | done (2026-11-23, merged in #6): 19 abilities, 100 mutations, 5 foci, 8 descriptors, Cap. 18 rebuilt in OG's order, 15 creatures, 5 NPCs, linking pass |
| WP7 | OG editorial content (~68k) | in progress (2026-11-23, `wp7-og`): sections that WP4–WP6 links waited for done; all their pending links resolved; Ch1/Ch3/Ch4/Ch5 additions, sentence generator, KUR-CSCS and KUR-CSSK sheets done; Ch6/Ch7 done; Ch8 done; Ch9 done (Errata and OG-variant abilities, category lists rebuilt with six new categories, 81 notes and sidebars); Ch10 done (five OG optional rules, armor table, quick references); Ch11 done (14 OG rule additions, difficulty dial, 25 notes); Ch11-A done (followers additions, Sidekicks as Camaradas); Ch12 done (five OG advancement rules, XP spending quick reference, 4 notes); Ch13 done (supernatural limits rule, four quick references, 7 notes, Cap. 11 lists sorted); Ch14 done (OG price tables with Invaluables, 2 notes, quick references); Ch14-A done (quick reference only); Ch14-B done (already complete; one list sorted); Ch15 done (Cap. 13 reordered like OG, space hazards moved from Cap. 9, S&E section and piloting intrusions, 7 notes); Ch16 done (Cap. 16 reordered, Stress and Serious Injuries translated, horror foci); Ch17 done (structure, 1 note); Ch18 done (Cap. 14 old/new CSRD merged like OG, power shifts in other genres, transformations, superhero foci); Ch19 checked (already complete); Claim the Sky archetype list removed; Ch20 done (Cap. 15 reordered like OG, 28 sidebars boxed, 2 notes, 15 fixes); Ch21 done (Cap. 19 order, 1 note, tú forms); Ch21-A checked (two sidebars boxed, vices quick reference grouped); Ch22 done (Creatures and NPCs index, fantasy table to Cap. 11, GM intrusions boxed, 4 notes); Ch23 done (Supervillano entry, by-level boxes, GM intrusions boxed, 7 notes); Ch24 done (Cap. 22 restructured like OG, OG's resolving box, sidebars boxed, 5 notes); Ch25 done (Cap. 23 in OG's order, 11 OG sections translated incl. campaign checklist, session prep, teaching the rules, making meaning, creating options and the example of play, 12 notes); back matter done (Cypher cortos and Atrapado en llamas matched to OG, FAQ translated, Índice with OG's optional rules index; no pending links left) |
| WP8 | Structural integration (renumbering, duplicate ids) | done (2026-11-23, `wp7-og`): Part 3 in OG's order; OG's chapter numbers (Cap. 1 Notas de la traducción, Cap. 2 Licencia … Cap. 25); TOC and navbar updated; duplicate ids 118 → 0; Cap. 13 creature lists merged |
| WP9 | QA and release, ODT/PDF | in progress (2026-11-22, `wp2-gaps`): `CORRECCIONES.json` applied to the ODT (386 fixes), PDF regenerated |

## Chapters

| OG-CSRD chapter | DRSC-ES chapter | Covered books | Still to translate (EN words, WP) | Status |
|---|---|---|---|---|
| Ch1 Foreword | Cap. 1 Notas de la traducción (*Acerca de esta edición*) | — | OG editorial 0.5k (WP7) | done (WP7) |
| Ch2 Open License | Cap. 2 Licencia | complete | — | done |
| Ch3 How to Play | Cap. 3 Cómo jugar | complete | — | done |
| Ch4 Creating Your Character | Cap. 4 Creación de personajes | complete | OG editorial 2.1k (WP7) | done (WP7) |
| Ch5 Type | Cap. 5 Tipos | complete | OG editorial 1.5k (WP7) | done (WP7) |
| Ch6 Flavor | Cap. 6 Aspectos | complete (5 IOM flavors added in WP3) | OG editorial 0.5k (WP7) | done (WP7) |
| Ch7 Descriptor | Cap. 7 Descriptores | complete | OG editorial 3.0k (WP7) | done (WP7) |
| Ch8 Focus | Cap. 8 Rasgos | complete (10 IOM foci added in WP3) | 21 foci: NR 3.0k, HNAM 2.4k, RR 1.9k (WP4–6); OG editorial 3.5k (WP7) | done (WP7) |
| Ch9 Abilities | Cap. 9 Capacidades + Listado | complete (125 IOM abilities and cantrips added in WP3) | 243 abilities: NR 3.9k, HNAM 4.5k, RR 9.7k (WP4–6); OG editorial 5.0k, including 16 "Errata" (old) abilities (WP7) | done (WP7) |
| Ch10 Equipment | Cap. 10 Equipo | complete (Reviving Artifacts added in WP3) | OG editorial 0.8k (WP7) | done (WP7) |
| Ch11 Rules of the Game | Cap. 11 Reglas del juego | complete (NR Ultimate Damage and High-Speed Chases added in WP4) | OG editorial 2.6k (WP7) | done (WP7) |
| Ch11-A Followers and Factions | Cap. 11-A Seguidores y facciones | complete (Familiars and Covens added in WP3) | OG editorial 10.2k, Sidekicks (WP7) | done (WP7) |
| Ch12 Experience Points | Cap. 12 Puntos de experiencia | complete (4 Heartwood arcs added in WP2; NR Splitting XP added in WP4) | OG editorial 1.9k (WP7) | done (WP7) |
| Ch13 Fantasy | Cap. 13 Fantasía | complete (IOM crafting additions merged in WP3) | OG editorial 1.5k (WP7) | done (WP7) |
| Ch14 Modern | Cap. 14 Moderno | complete | OG editorial 0.6k (WP7) | done (WP7) |
| Ch14-A Modern Magic | Cap. 14-A Magia moderna | complete (WP3) | — | done |
| Ch14-B Cyberpunk | Cap. 14-B Ciberpunk (WP4) | complete (links to sections not yet translated pending) | — | done |
| Ch15 Science Fiction | Cap. 15 Ciencia ficción | complete | OG editorial 1.2k (WP7) | done (WP7) |
| Ch16 Horror | Cap. 16 Horror | complete | OG editorial 4.1k (WP7) | done (WP7) |
| Ch17 Romance | Cap. 17 Romance | complete (NR Character Reputations and Relationships added in WP4) | — | done |
| Ch18 Superheroes | Cap. 18 Superhéroes | complete | OG editorial 1.7k (WP7) | done (WP7) |
| Ch19 Post-Apocalyptic | Cap. 19 Post-apocalíptico | complete (the 0.68 ratio is R&R text OG merged into Scavenging) | RR 17.3k, including the revised Scavenging and the Mutant descriptor (WP6) | done (WP6) |
| Ch20 Fairy Tale | Cap. 20 Cuentos de hadas | complete | OG structure and notes (WP7) | done (WP7) |
| Ch21 Historical | Cap. 21 Histórico | complete | OG structure and note (WP7) | done (WP7) |
| Ch21-A Weird West | Cap. 21-A Oeste extraño (WP5) | complete | — | done |
| Ch22 Creatures | Cap. 22 Criaturas | complete (13 IOM creatures added in WP3, 11 HNAM in WP5, 15 RR in WP6) | 15 creatures: RR 5.0k (WP6) | done (WP6) |
| Ch23 NPCs | Cap. 23 PNJs | complete (4 IOM NPCs added in WP3, 2 HNAM in WP5, 5 RR in WP6) | 5 NPCs: RR 1.3k (WP6) | done (WP6) |
| Ch24 Cyphers | Cap. 24 Cyphers | complete | RR 0.1k (WP6); OG editorial 0.9k (WP7) | done (WP7) |
| Ch25 Running the Cypher System | Cap. 25 Dirigir el Sistema Cypher | complete | HNAM 0.1k, RR 0.3k (WP5, 6); OG editorial 14.4k (WP7) | done (WP7) |
| Cypher Shorts | Inicio rápido: Cypher cortos | complete | — | done |
| Trapped in Flames | Aventura: Atrapado en llamas | complete | — | done |
| FAQ | Preguntas frecuentes (Parte 5) | — | OG editorial 3.5k (WP7) | done (WP7) |
| OG-CSRD Index | Índice (Parte 5) | — | OG editorial 1.0k (WP7) | done (WP7) |
| What's in the Book | — (new) | — | OG editorial 5.6k (WP7) | left out (decision, 2026-11-23) |

## Terminology decisions

Settled 2026-11-22 before WP3; see `GLOSARIO.md` › *Decisiones tomadas* and *Magia moderna
(It's Only Magic)*. Add new open questions to `GLOSARIO.md` before translating the chapter that
needs them.
