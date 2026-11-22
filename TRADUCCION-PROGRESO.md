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
| WP2 | Gaps inside covered books, CSRD 2025 errata | in progress (2026-11-22, `wp2-gaps`): range/distance terminology normalised (including five range-band errors) |
| WP3 | It's Only Magic (~44k) | to do |
| WP4 | Neon Rain (~42k) | to do |
| WP5 | High Noon at Midnight (~38k) | to do |
| WP6 | Rust and Redemption (~36k) | to do |
| WP7 | OG editorial content (~68k) | to do |
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
| Ch6 Flavor | Cap. 4 Aspectos | complete | IOM 0.5k, 5 flavors (WP3); OG editorial 0.5k (WP7) | to do |
| Ch7 Descriptor | Cap. 5 Descriptores | complete | OG editorial 3.0k (WP7) | to do |
| Ch8 Focus | Cap. 6 Rasgos | 6 Heartwood foci missing (WP2) | 31 foci: IOM 3.5k, NR 3.0k, HNAM 2.4k, RR 1.9k (WP3–6); OG editorial 3.5k (WP7) | to do |
| Ch9 Abilities | Cap. 7 Capacidades + Listado | Moonbeam and Question Past Self missing; 16 errata abilities (WP2) | 367 abilities: IOM 14.2k, NR 3.9k, HNAM 4.5k, RR 9.7k (WP3–6); OG editorial 5.0k (WP7) | to do |
| Ch10 Equipment | Cap. 8 Equipo | complete | IOM 0.2k (WP3); OG editorial 0.8k (WP7) | to do |
| Ch11 Rules of the Game | Cap. 9 Reglas del juego | complete | NR 1.1k (WP4); OG editorial 2.6k (WP7) | to do |
| Ch11-A Followers and Factions | Cap. 9-A Seguidores y facciones | complete | IOM 2.2k, Familiars and Covens (WP3); OG editorial 10.2k, Sidekicks (WP7) | to do |
| Ch12 Experience Points | Cap. 10 Puntos de experiencia | complete | NR 0.4k (WP4); OG editorial 1.9k (WP7) | to do |
| Ch13 Fantasy | Cap. 11 Fantasía | complete | IOM 0.1k (WP3); OG editorial 1.5k (WP7) | to do |
| Ch14 Modern | Cap. 12 Moderno | complete | OG editorial 0.6k (WP7) | to do |
| Ch14-A Modern Magic | — (new chapter) | — | IOM 15.5k (WP3) | to do |
| Ch14-B Cyberpunk | — (new chapter) | — | NR 33.5k (WP4) | to do |
| Ch15 Science Fiction | Cap. 13 Ciencia ficción | complete | OG editorial 1.2k (WP7) | to do |
| Ch16 Horror | Cap. 16 Horror | complete | OG editorial 4.1k (WP7) | to do |
| Ch17 Romance | Cap. 17 Romance | complete | NR 0.1k (WP4) | to do |
| Ch18 Superheroes | Cap. 14 Superhéroes | complete | OG editorial 1.7k (WP7) | to do |
| Ch19 Post-Apocalyptic | Cap. 18 Post-apocalíptico | check Carroñeo against OG Scavenging; chapter is 0.68 × OG (WP2) | RR 17.3k (WP6) | to do |
| Ch20 Fairy Tale | Cap. 15 Cuentos de hadas | 6 Heartwood descriptors missing (WP2) | — | to do |
| Ch21 Historical | Cap. 19 Histórico | complete | — | done |
| Ch21-A Weird West | — (new chapter) | — | HNAM 25.2k (WP5) | to do |
| Ch22 Creatures | Cap. 20 Criaturas | complete | 39 creatures: IOM 6.5k, HNAM 4.7k, RR 5.0k (WP3, 5, 6) | to do |
| Ch23 NPCs | Cap. 21 PNJs | complete | 11 NPCs: IOM 1.2k, HNAM 0.9k, RR 1.3k (WP3, 5, 6) | to do |
| Ch24 Cyphers | Cap. 22 Cyphers | complete | RR 0.1k (WP6); OG editorial 0.9k (WP7) | to do |
| Ch25 Running the Cypher System | Cap. 23 Dirigir el Sistema Cypher | complete | HNAM 0.1k, RR 0.3k (WP5, 6); OG editorial 14.4k (WP7) | to do |
| Cypher Shorts | Cap. 24 Cypher cortos | complete | — | done |
| Trapped in Flames | Aventura: Atrapado en llamas | complete | — | done |
| FAQ | — (new) | — | OG editorial 3.5k (WP7) | to do |
| OG-CSRD Index | — (new) | — | OG editorial 1.0k (WP7) | to do |
| What's in the Book | — (new) | — | OG editorial 5.6k (WP7) | to do |

## Terminology decisions

Open decisions are listed in `GLOSARIO.md` › *Decisiones pendientes*. Settle them before
WP3 so the new chapters use one term from the start.
