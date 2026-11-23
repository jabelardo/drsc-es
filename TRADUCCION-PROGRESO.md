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
| WP7 | OG editorial content (~68k) | in progress (2026-11-23, `wp7-og`): sections that WP4–WP6 links waited for done; all their pending links resolved; Ch1/Ch3/Ch4/Ch5 additions, sentence generator, KUR-CSCS and KUR-CSSK sheets done; Ch6/Ch7 done; Ch8 done; Ch9 done (Errata and OG-variant abilities, category lists rebuilt with six new categories, 81 notes and sidebars); Ch10 done (five OG optional rules, armor table, quick references); Ch11 done (14 OG rule additions, difficulty dial, 25 notes); Ch11-A done (followers additions, Sidekicks as Camaradas) |
| WP8 | Structural integration (renumbering, duplicate ids) | to do |
| WP9 | QA and release, ODT/PDF | in progress (2026-11-22, `wp2-gaps`): `CORRECCIONES.json` applied to the ODT (386 fixes), PDF regenerated |

## Chapters

| OG-CSRD chapter | DRSC-ES chapter | Covered books | Still to translate (EN words, WP) | Status |
|---|---|---|---|---|
| Ch1 Foreword | — | — | OG editorial 0.5k (WP7) | to do |
| Ch2 Open License | El Sistema Cypher › Licencia | complete | — | done |
| Ch3 How to Play | Cap. 1 Cómo jugar | complete | — | done |
| Ch4 Creating Your Character | Cap. 2 Creación de personajes | complete | OG editorial 2.1k (WP7) | to do |
| Ch5 Type | Cap. 3 Tipos | complete | OG editorial 1.5k (WP7) | to do |
| Ch6 Flavor | Cap. 4 Aspectos | complete (5 IOM flavors added in WP3) | OG editorial 0.5k (WP7) | to do |
| Ch7 Descriptor | Cap. 5 Descriptores | complete | OG editorial 3.0k (WP7) | to do |
| Ch8 Focus | Cap. 6 Rasgos | complete (10 IOM foci added in WP3) | 21 foci: NR 3.0k, HNAM 2.4k, RR 1.9k (WP4–6); OG editorial 3.5k (WP7) | to do |
| Ch9 Abilities | Cap. 7 Capacidades + Listado | complete (125 IOM abilities and cantrips added in WP3) | 243 abilities: NR 3.9k, HNAM 4.5k, RR 9.7k (WP4–6); OG editorial 5.0k, including 16 "Errata" (old) abilities (WP7) | to do |
| Ch10 Equipment | Cap. 8 Equipo | complete (Reviving Artifacts added in WP3) | OG editorial 0.8k (WP7) | to do |
| Ch11 Rules of the Game | Cap. 9 Reglas del juego | complete (NR Ultimate Damage and High-Speed Chases added in WP4) | OG editorial 2.6k (WP7) | to do |
| Ch11-A Followers and Factions | Cap. 9-A Seguidores y facciones | complete (Familiars and Covens added in WP3) | OG editorial 10.2k, Sidekicks (WP7) | to do |
| Ch12 Experience Points | Cap. 10 Puntos de experiencia | complete (4 Heartwood arcs added in WP2; NR Splitting XP added in WP4) | OG editorial 1.9k (WP7) | to do |
| Ch13 Fantasy | Cap. 11 Fantasía | complete (IOM crafting additions merged in WP3) | OG editorial 1.5k (WP7) | to do |
| Ch14 Modern | Cap. 12 Moderno | complete | OG editorial 0.6k (WP7) | to do |
| Ch14-A Modern Magic | Cap. 12-A Magia moderna | complete (WP3) | — | done |
| Ch14-B Cyberpunk | Cap. 12-B Ciberpunk (WP4) | complete (links to sections not yet translated pending) | — | done |
| Ch15 Science Fiction | Cap. 13 Ciencia ficción | complete | OG editorial 1.2k (WP7) | to do |
| Ch16 Horror | Cap. 16 Horror | complete | OG editorial 4.1k (WP7) | to do |
| Ch17 Romance | Cap. 17 Romance | complete (NR Character Reputations and Relationships added in WP4) | — | done |
| Ch18 Superheroes | Cap. 14 Superhéroes | complete | OG editorial 1.7k (WP7) | to do |
| Ch19 Post-Apocalyptic | Cap. 18 Post-apocalíptico | complete (the 0.68 ratio is R&R text OG merged into Scavenging) | RR 17.3k, including the revised Scavenging and the Mutant descriptor (WP6) | done (WP6) |
| Ch20 Fairy Tale | Cap. 15 Cuentos de hadas | complete | — | done |
| Ch21 Historical | Cap. 19 Histórico | complete | — | done |
| Ch21-A Weird West | Cap. 19-A Oeste extraño (WP5) | complete | — | done |
| Ch22 Creatures | Cap. 20 Criaturas | complete (13 IOM creatures added in WP3, 11 HNAM in WP5, 15 RR in WP6) | 15 creatures: RR 5.0k (WP6) | done (WP6) |
| Ch23 NPCs | Cap. 21 PNJs | complete (4 IOM NPCs added in WP3, 2 HNAM in WP5, 5 RR in WP6) | 5 NPCs: RR 1.3k (WP6) | done (WP6) |
| Ch24 Cyphers | Cap. 22 Cyphers | complete | RR 0.1k (WP6); OG editorial 0.9k (WP7) | to do |
| Ch25 Running the Cypher System | Cap. 23 Dirigir el Sistema Cypher | complete | HNAM 0.1k, RR 0.3k (WP5, 6); OG editorial 14.4k (WP7) | to do |
| Cypher Shorts | Cap. 24 Cypher cortos | complete | — | done |
| Trapped in Flames | Aventura: Atrapado en llamas | complete | — | done |
| FAQ | — (new) | — | OG editorial 3.5k (WP7) | to do |
| OG-CSRD Index | — (new) | — | OG editorial 1.0k (WP7) | to do |
| What's in the Book | — (new) | — | OG editorial 5.6k (WP7) | to do |

## Terminology decisions

Settled 2026-11-22 before WP3; see `GLOSARIO.md` › *Decisiones tomadas* and *Magia moderna
(It's Only Magic)*. Add new open questions to `GLOSARIO.md` before translating the chapter that
needs them.
