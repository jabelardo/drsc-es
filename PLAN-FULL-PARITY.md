# Plan for Full Parity: DRSC-ES → OG-CSRD

Status: in execution. WP1 is complete on branch `wp1-fantasy-relocation` and WP0 on
`wp0-setup`; both are ready to merge (see §5; last updated 2026-11-22). Per-chapter status
is tracked in `TRADUCCION-PROGRESO.md`. The plan was revised on 2026-11-22 after a
source-attribution audit (§3).
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
   equivalent rules content (not necessarily identical wording), **in the same place
   in the structure** (existing Spanish material is moved, not retranslated).
2. All new material is fully translated, not machine-pasted, using the existing
   Spanish terminology and the `[English]` bilingual label convention.
3. Every new heading has an id and a permalink anchor; every internal link resolves.
   Ids of moved sections are kept, so existing inbound links keep working.
4. TOC, navbar dropdowns, quick-reference boxes, part colours and theme styling
   cover all new/expanded chapters.
5. The Index, FAQ, What's in the Book and other OG editorial/tool sections exist
   in Spanish.
6. No ES-only content is lost (Cypherpunk/Dark Sun extras and the translator's
   notes are preserved).
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
- **Rules wording comes from the CSRD file, not OG** (learned in WP2). OG-CSRD
  sometimes edits CSRD text without marking it (e.g. *Secret and True Names*, the
  Giant Spider). Take structure from OG, but check every paragraph you translate
  against `Cypher-System-Reference-Document-2025-08-22.docx`.
- **Keep OG-CSRD's notes** (decided 2026-11-22). Translate OG's sidebars and editor's
  notes with the content they belong to, even when the CSRD lacks them: they add
  clarifications. Label editor's notes *Nota del editor:*. When extracting, take
  every paragraph (including OG's indented `og-ind` ones) and the sidebars and notes that
  follow each entry.
  - Exception (decided 2026-11-22): leave out notes that point to *Old Gus' Daft
    Drafts* (OG's external `og-dd.html` page). Where a note also says something else,
    keep that part and drop only the Daft Drafts reference.
  - OG-only additions are not labelled in the text (the user removed the
    *Adición editorial de OG-CSRD.* markers on 2026-11-22).
- **Terminology:** reuse the existing DRSC-ES glossary; keep English names in
  `[brackets]` exactly as the current document does.
- **Editorial policy:** full parity includes OG editorial content (foreword, editor
  notes, page citations, "Related Sections", Index, FAQ, What's in the Book,
  Character Sentence Generator, PDFs/Player's Guide links). Where OG makes an
  editorial ruling that differs from the official CSRD, preserve the official rules
  wording. OG's editor's notes keep the *Nota del editor:* label; OG-only sections are
  not labelled (decided 2026-11-22).

---

## 3. Current gap summary

### 3.1 Method

The earlier version of this section compared word counts chapter by chapter. That
made content OG keeps in a different chapter look like a gap in one place and a
surplus in another (for example "Fantasía: partial" next to "Ciencia ficción: ES
ahead"). This revision attributes content by source instead:

- OG-CSRD tags every section with its source book (`og-cite`), and every ability
  with an inline reference (`(122)`, `(IOM, 45)`, `(NR, 33)`…). Each OG section was
  classified as: from a book DRSC-ES already translates, from a book DRSC-ES does
  not cover, or an OG editorial addition.
- 821 of the 852 DRSC-ES headings that carry an `[English Name]` match an OG heading
  by name. The other 31 are spelling or naming variants and all have an OG
  counterpart, except the two entries listed in §3.6. The OG location of each
  matched heading was recorded.
- Unbracketed rules sections were compared heading by heading for every chapter.

Word counts below are English words in OG-CSRD and are approximate; they include
OG's inline page references.

### 3.2 Finding

**DRSC-ES already contains essentially all OG-CSRD content from the books it is based
on.** About 377k English words of OG come from those books, and DRSC-ES has about 387k
Spanish words. The apparent gaps and surpluses are almost entirely relocations: the
Spanish document follows the CSRD 2023 and supplement layout, and OG regroups that
material by topic.

What is actually missing falls into three groups:

| Group | EN words | Notes |
|---|---:|---|
| Four supplements not covered by DRSC-ES | ~159k | It's Only Magic ~44k, Neon Rain ~42k, High Noon at Midnight ~38k, Rust and Redemption ~36k |
| OG editorial additions (not CSRD text) | ~68k | Includes Index ~1k and What's in the Book ~6k (mostly generated lists), FAQ ~3.5k, Foreword ~0.5k |
| Gaps inside books DRSC-ES already covers | ~3k + errata | 12 We Are All Mad Here (Heartwood) entries listed by name only; CSRD 2023→2025 text revisions |

### 3.3 Existing Spanish material that OG keeps elsewhere (relocation map)

| Current DRSC-ES location | Content | OG-CSRD target | WP1 status |
|---|---|---|---|
| Módulo de reglas mágicas (~11.8k ES words) | Crafting magic items, magical technology, mystical martial arts, ritual magic, secret/true names, wishes, awarding treasure, dungeons/castles/keeps and traps | Ch13 Fantasy | Done |
| Módulo de reglas mágicas › Control mental, Posesión | Mind control, possession | Ch16 Horror › Horror Rules (Posesión is already duplicated in Cap. 16, so merge) | Done (Posesión merged) |
| Cap. 3 Tipos › Opciones de personajes de fantasía | Sorcerer, Warlock or Witch, Wizard, Wild Mage, etc. | Ch13 › Fantasy Character Options | Done |
| Cap. 8 Equipo › fantasy weapon/armor/clothing/adventuring-gear descriptions, medieval price categories | Medieval equipment | Ch13 › Medieval Fantasy Equipment | Done |
| Cap. 22 Cyphers › Cyphers de fantasía | Fantasy cyphers | Ch13 › Fantasy Cyphers | Done |
| Cap. 23 Dirigir › Artefactos › Artefactos de fantasía (~6.9k) | Fantasy artifacts | Ch13 › Fantasy Artifacts | Done |
| Cap. 20 Criaturas › Otras criaturas y PNJs para un juego de fantasía | Fantasy creature/NPC list | Ch13 › Basic Creatures and NPCs for a Fantasy Game | Done. *Criaturas y PNJs de fantasía por nivel* stays in Criaturas, because OG keeps its by-level list in Ch22 |
| Cap. 9 Reglas › Seguidores | Followers | Ch11-A Followers and Factions | Done (new Capítulo 9-A *Seguidores y facciones*) |
| Cap. 13 Ciencia ficción › GM-intrusion tables for wheeled, hovering/flying, sea and space vehicles | Vehicle GM intrusions | Ch11 › Action: Do Something Else › Riding or Piloting | Done (all four tables, under *Montar o pilotar*) |
| Cap. 13 Ciencia ficción › every category's "Contemporáneo" group (equipment, weapons, vehicles) and the pioneer-era spacecraft | Contemporary equipment and vehicles | Ch14 Modern › Additional Modern Equipment / Modern Vehicles | Done (11 equipment groups and a new *Vehículos modernos* section) |
| Cap. 13 Ciencia ficción › Criaturas y PNJs básicos (~12.2k) | SF creature and NPC stat blocks | Ch22 Creatures / Ch23 NPCs (genre chapter keeps the "Basic Creatures and NPCs" list) | Done (by-level table stays in Cap. 13) |
| Cap. 16 Horror › Criaturas y PNJs de horror por nivel y género (~5.4k), PNJs | Horror stat blocks | Ch22 / Ch23 | Done (by-level table stays in Cap. 16) |
| Cap. 15 Cuentos de hadas › Bestias y seres (~15.9k) | Fairy-tale stat blocks | Ch22 / Ch23 (Ch20 keeps the Beasts and Beings overview: magical animals, talking objects, beings by archetype) | Done (inline beings, archetype lists and PNJs intro stay in Cap. 15; Sátiro, Hada and Bruja keep both versions, §3.6) |
| Cap. 20 Criaturas › Supervillanos (~2.7k) and NPC entries filed as creatures | Supervillains, NPCs | Ch23 NPCs (Ch18 keeps the Supervillains overview) | Done (Supervillanos moved whole, after Otros PNJs) |
| Cap. 14 Superhéroes › Cyphers y artefactos › Cyphers de refuerzo de potencia | Three Claim the Sky power-boost cyphers and the d100 power-boost table | Ch24 › Power Boost Cyphers / Power Boost Cypher Table | Done (found by the final WP1 check; not in the original audit) |

Everything else in DRSC-ES sits in the OG chapter it maps to. Fairy-tale cyphers and
artifacts already live in the Fairy Tale chapter in both documents.

With these moves, the earlier "partial" and "ES ahead" chapters reconcile. Fantasy,
Modern, Science Fiction, Horror, Fairy Tale, Creatures and NPCs are complete for the
books DRSC-ES covers. Their remaining gaps are the supplement and OG-editorial rows
in §3.4.

### 3.4 What is actually missing, per OG chapter

| OG chapter | Missing supplement content (EN words) | OG editorial (EN words) |
|---|---|---:|
| Ch1 Foreword | — | 0.5k |
| Ch4 Creating Your Character | — | 2.1k (effort cost tables, optional rules, sentence generator, checklist, PDFs) |
| Ch5 Type | — | 1.5k |
| Ch6 Flavor | 0.5k IOM (5 flavors) | 0.5k |
| Ch7 Descriptor | (genre descriptors counted in genre chapters) | 3.0k (descriptor lists from other products) |
| Ch8 Focus | 10.9k (31 foci: IOM 10, NR 9, HNAM 7, R&R 5) | 3.5k |
| Ch9 Abilities | 32.1k (367 abilities: IOM 125, R&R 120, HNAM 73, NR 49; cantrips IOM; mutations R&R) | 5.0k (extra categories, Stress abilities, errata list) |
| Ch10 Equipment | 0.2k IOM | 0.8k (5 optional rules) |
| Ch11 Rules of the Game | 1.1k NR | 2.6k (optional rules) |
| Ch11-A Followers and Factions | 2.2k IOM (Familiars, Covens) | 10.2k (Sidekicks, followers vs. companions) |
| Ch12 Experience Points | 0.4k NR (Splitting XP) | 1.9k (XP advance, tier 0, slower advancement, beyond tier 6) |
| Ch13 Fantasy | 0.1k IOM | 1.5k |
| Ch14 Modern | — | 0.6k (mundane foci, priceless items) |
| Ch14-A Modern Magic | 15.5k IOM (whole chapter) | 0.1k |
| Ch14-B Cyberpunk | 33.5k NR (whole chapter) | 0.4k |
| Ch15 Science Fiction | — | 1.2k |
| Ch16 Horror | — | 4.1k (Stress, Serious Injuries and Conditions, horror foci list) |
| Ch17 Romance | 0.1k NR | — |
| Ch18 Superheroes | — | 1.7k |
| Ch19 Post-Apocalyptic | 17.3k R&R (character options, equipment, optional rules, cyphers, artifacts) | 0.1k |
| Ch21-A Weird West | 25.2k HNAM (whole chapter) | 0.5k |
| Ch22 Creatures | 16.2k (39 creatures: R&R 15, IOM 13, HNAM 11) | — |
| Ch23 NPCs | 3.5k (11 NPCs: R&R 5, IOM 4, HNAM 2) | — |
| Ch24 Cyphers | 0.1k R&R | 0.9k |
| Ch25 Running the Cypher System | 0.4k | 14.4k (campaign checklist, session prep, teaching the rules, making meaning, example of play, creating creatures/options) |
| FAQ / Index / What's in the Book | — | 3.5k / 1.0k / 5.6k |

Chapters with nothing missing from either column: Ch2 Open License, Ch3 How to Play,
Ch20 Fairy Tale (except the Heartwood entries below), Ch21 Historical, Cypher Shorts,
Trapped in Flames.

Gaps inside books DRSC-ES already covers:

- **Heartwood (We Are All Mad Here).** Cap. 15 lists these only by name with page
  references ("Descriptores de Heartwood", "Rasgos de Heartwood"). OG has the full
  text (~2.9k EN words):
  - 6 descriptors: Bewitched, Changeling, Fragmented, Frumious, Haunted, Lost.
  - 6 foci: Befriends the Black Dog, Curses the World, Feigns No Fear, Lived Among
    the Fey, Made a Deal With Death, Sheds Their Skin.
- **CSRD 2025 text revisions.** Rules text that changed between the CSRD of
  2023-04-18 and 2025-08-22. The WP0 audit found missing abilities:
  - 16 abilities OG cites as *Errata*: Chop, Crush, Daring Escape, Extra Edge, Font of
    Inspiration, Mighty Blow, Opening Gambit, Practiced With Light (and Medium) Weapons,
    Riposte, Seize Opportunity, Shooting Gallery, Skills, Slayer, Specialization,
    Surprise Strike. *Resolved in WP2:* these are old 2015-Rulebook versions that OG
    keeps for compatibility, so they are OG editorial (WP7), not CSRD gaps.
  - 2 abilities not in DRSC-ES: Moonbeam and Question Past Self. *Added in WP2;* they
    turned out to be It's Only Magic abilities that OG cites with bare page numbers.
  - A direct diff of the 2023 and 2025 CSRD files shows no changed wording in existing
    text: the 2025 CSRD only adds material; see WP2.
- **Mutant descriptor** (post-apocalyptic). *Resolved in WP2:* OG cites it as Rust and
  Redemption, page 116 (WP6).

### 3.5 Revised entry-level gaps

| Item | Missing | From the four supplements | Other |
|---|---:|---:|---|
| Abilities | ~370 + lists | 367 + cantrips (IOM) + mutations (R&R) | ~80 OG editorial (Stress abilities etc.) |
| Foci | 37 | 31 | 6 Heartwood (WAAMH) |
| Descriptors | ~37 | 30 (HNAM 10, R&R 8, IOM 7, NR 5) | 6 Heartwood (WAAMH), Mutant (verify) |
| Flavors | 5 | 5 (IOM: Charms and Figments, Cozy Magic, Divination, Modern Magic, Protection) | + 2 OG optional rules (simplified, personalized flavor) |
| Optional rules | ~58 | 12 (NR 6, R&R 4, IOM 2) | 46 OG editorial |
| Creatures | 39 | 39 | — |
| NPCs | 11 | 11 | — (the "NPCs mostly missing" reading came from NPCs filed in genre chapters) |
| Cyphers | parity | supplement cyphers ship with their genre chapters | — |

### 3.6 ES-only content and anomalies

- ES-only, to keep: Extras (Cypherpunk / Dark Sun PDFs, `contrib/`) and *Notas de la
  traducción*.
- Checked in WP2:
  - *Estabilizador mental [Mind Stabilizer]* (cypher, Cap. 22) is in OG, misspelled
    "Mind Stablizer" (Rulebook, page 393). Keep.
  - *Escudo deflector [Deflecting Shield]* (fantasy artifact, Cap. 23): OG says the
    deflecting shield (Godforsaken, page 150) is not included in the CSRD, and lists
    the Truth Binoculars (*Prismáticos de la verdad*, already in DRSC-ES) in its place
    in the Minor Fantasy Artifacts table. Both CSRD files list it by name only, with no
    description. **Decided 2026-11-22: keep** the entry and the table row as they are.
- Duplicates to consolidate:
  - *Posesión*: **done in WP1.** The Cap. 16 section is kept, with the module's opening
    sentence and consent paragraph merged in, as in OG. The module's `posesion` id
    remains as an alias.
  - *Locura*: **done in WP1.** The encyclopedia entry now holds the full optional-rule
    text, as OG's single Madness section; the one-paragraph summary and the separate
    *Regla opcional: Locura* section are gone, and its id remains as an alias.
- Heading bug: *Jotunn (gigante nórdico)* was an h4 in Cap. 20, so every creature after
  it was nested under it. **Fixed in WP1:** Jotunn is now one NPC entry in Cap. 21 (h5),
  with its fire and frost variants as h6 sub-entries, as in OG.
- Found and fixed during WP1:
  - The second *Artefactos de fantasía* heading in Cap. 11 is now *Listado de artefactos
    de fantasía*.
  - *Más hechos* → *Más hechizos*; *Cuéntos* / *hádas* → *Cuentos* / *hadas*.
  - Moving entries changed which element four duplicated ids resolved to (`bruja`,
    `hada`, `satiro`, `espectro`). The shadowed alias spans were dropped so each id has
    its pre-WP1 target again, and the fantasy/horror by-level tables now link to the
    core/Godforsaken entries they list.
  - The Munición group reused Ocio's id `contemporaneo-6`; it now uses the unused
    `contemporaneo-7`.
  - Criaturas and PNJs sort ignoring a leading El/La/Los/Las (decided 2026-11-22).
    Accents are ignored, but ñ sorts after n (*Canto* before *Cañón*), as in the
    existing Cap. 7 lists. The Cap. 7 ability lists sort letter by letter, ignoring
    spaces and punctuation (*Ahí está tu problema* before *A la defensiva*), as the
    original lists did; re-sorted on 2026-11-23 after WP3 and WP4 insertions had used
    word-by-word order.
  - Duplicate ids are down from 134 to 127.
- Decided (2026-11-22): keep both versions of *Sátiro*, *Hada* and *Bruja* rather than
  merging them as OG does for Hada and Bruja. Each pair is the same creature at the same
  level but written differently (description, environment, abilities). The core or
  Godforsaken version keeps the plain name; the We Are All Mad Here version is labelled
  *(Cuentos de hadas)*. The two versions sit next to each other in Criaturas/PNJs.
- Still open:
  - `#control-mental` is the id of both the Control mental ability and the Horror
    section, so links meant for the section (e.g. in Posesión) open the ability.
    Resolve with the duplicate-id clean-up in WP8.
  - `#botas-de-saltar` is used by three different items; the fairy-tale table link
    opens the fantasy artifact. Resolve in WP8.

---

## 4. Target structure

Adopt the OG-CSRD five-part structure and English chapter order. The magic-rules module
and the stat blocks in genre chapters are redistributed per §3.3; only the Extras
remain as an appendix.

- Part 0 / front: Prólogo (Foreword), Licencia, Notas de la traducción, Cómo jugar.
- Part 1 Characters: Creación, Tipos, Aspectos, Descriptores, Rasgos, Capacidades,
  Equipo.
- Part 2 Rules: Reglas del juego, Seguidores y facciones, Puntos de experiencia.
- Part 3 Genres: Fantasía, Moderno, Magia moderna, Cyberpunk, Ciencia ficción,
  Horror, Romance, Superhéroes, Post-apocalíptico, Cuentos de hadas, Histórico,
  Oeste extraño.
- Part 4 Game Mastering: Criaturas, PNJs, Cyphers, Dirigir el Sistema Cypher.
- Part 5 Back matter: Cypher cortos, Atrapado en llamas, FAQ, Índice,
  Qué hay en el libro.
- Appendix (ES-only, preserved): Extras (Cypherpunk / Dark Sun PDFs).

Renumber chapters to match the final order and update the TOC and navbar.

---

## 5. Work packages

Translation work is organised by source book. Each book's foci, abilities,
descriptors, creatures and NPCs are spread across several OG chapters but share
terminology, so translating a book in one pass keeps them consistent.

### WP0 — Setup (0.5–1 day) — done on branch `wp0-setup`
- [x] Record the locked source version in the document header: *Estructura según
      OG-CSRD v2.11a (2026-08-14), basado en el CSRD del 2025-08-22*.
- [x] Create `GLOSARIO.md` (EN→ES term map) and `TRADUCCION-PROGRESO.md`
      (per-chapter status).
      - The glossary's core terms are hand-written from the document's actual usage.
      - Its ~1,960 named elements are generated by `tools/parity/glossary.py`.
      - It records the range/distance rule decided on 2026-11-22: range is *alcance*,
        distance is *distancia*, as English distinguishes them.
      - It lists two open terminology decisions ("training", *Aspecto*) and one likely
        inconsistency: *Infiltrator* is *Infiltrado* as an ability and *Infiltrador* as
        a cypher.
- [x] Add QA scripts (`tools/qa/`):
      - `check_html.py`: anchors, duplicate ids, tag structure, heading levels. With
        `--baseline REF` it adds an id diff, a word diff, and duplicated ids whose
        target element changed.
      - `render.py`: headless Chrome in light and dark, for the whole page or one
        section, failing on unexpected console messages.
      - Usage is in `tools/README.md`. `.gitignore` now tracks `tools/**/*.py`.
- [x] Add the source-attribution audit (`tools/parity/audit.py`) so §3 can be re-run
      after each work package. It downloads OG-CSRD once into `.cache/` (git-ignored).

### WP1 — Reorganise existing Spanish content (no new translation, ~4–8 days) — done
- [x] Fantasy: Cap. 11 now follows OG Ch13 order.
      - Moved in: the magic module, fantasy type options, medieval equipment, fantasy
        cyphers, fantasy artifacts and the other fantasy creatures list.
      - *Hechizos preparados vs espontáneos* joined the spellcasting rule.
      - *Control mental* moved to the Horror encyclopedia, after *Locura*.
- [x] Sci-Fi and Horror stat blocks moved to Criaturas/PNJs.
      - Cap. 20 Criaturas now has 96 creatures in one alphabetical list.
      - Cap. 21 PNJs now has 43 NPCs, followed by *Supervillanos*. That includes the
        19 entries that were filed as creatures but are NPCs in OG (Goblin, Orco, Ogro,
        Trol, Bruja, Fada…).
      - The genre chapters keep their basic lists and by-level tables.
- [x] Fairy Tale stat blocks (*Bestias y seres*) moved to Criaturas/PNJs.
      - Criaturas now has 104 creatures; *Minotauro, el* is nested under *Minotáuro*,
        as in OG.
      - PNJs now has 60 NPCs, including three combined entries as in OG: *Encantador*
        (Morgan Le Fay, Oz, Virgilius), *Reina* (Grimilda, Roja, Nieves) and *Bruja
        (Cuentos de hadas)* (Baba Yaga and four more).
      - Cap. 15 keeps the inline beings (Bagheera, Gato Cheshire…), the archetype lists
        and the PNJs introduction, as OG Ch20 does.
      - The emptied *Encantadores del mundo* and *Brujas del mundo* headings remain as
        alias anchors.
- [x] Seguidores: new Capítulo 9-A *Seguidores y facciones* (OG Ch11-A) around the
      existing section, with its quick reference and TOC entry. The number is
      provisional until the WP8 renumbering.
- [x] The four vehicle GM-intrusion tables moved from Cap. 13 to Cap. 9 › *Montar o
      pilotar* (OG keeps all four in Rules, not only the spacecraft one).
- [x] Contemporary equipment and vehicles moved to Cap. 12 Moderno.
      - Each Sci-Fi category's "Contemporáneo" group moved, with its marker turned into
        the group heading. That gives 11 equipment groups and a new *Vehículos modernos*
        section with 5 vehicle groups plus the pioneer-era spacecraft.
      - Cap. 12 now follows OG order.
- [x] Consolidate Posesión and Locura; fix the Jotunn heading level.
- [x] Fix the small issues found during WP1 (§3.6), including the duplicate-id targets
      that the moves had changed.
- [x] Sort Criaturas and PNJs ignoring a leading El/La/Los/Las.
- [x] Keep both versions of Sátiro, Hada and Bruja, the We Are All Mad Here one
      labelled *(Cuentos de hadas)* (§3.6).
- [x] Superhero power-boost cyphers moved to Cap. 22. The final check found them:
      - Reforzador de eficacia, de mejora and de proeza joined the power-boost list
        (now all 11, as in OG).
      - The d100 table became *Tabla de Cyphers de refuerzo de potencia* under *Listado
        de Cyphers por categoría*.
- [x] Keep every moved section's id. Ids whose heading was dissolved remain as alias
      anchors:
      - `modulo-de-reglas-magicas` on *Artes marciales místicas*
      - `posesion` on the Horror *Posesión*
      - `regla-opcional-locura` on the encyclopedia *Locura*
      - `pnjs-1`, `creatures-2-list` and `npcs-1-list` in Cap. 16
      - `creatures-4-list` in Cap. 13
      - `encantadores-del-mundo`, `brujas-del-mundo` and the emptied fairy-tale list
        wrappers in Cap. 15
- [x] Update TOC, navbar, quick-reference boxes and cross-links after each move. The
      TOC gained the 9-A chapter; the navbar only links to chapters and needed no
      change.
- Final acceptance check against the pre-WP1 baseline (main at 2aafddb):
  - Of 818 Spanish headings whose English name matches OG, all sit in their OG
    chapter. The only flags are the inline fairy-tale beings *Enano* and *Trol*, which
    share names with NPC entries.
  - Each Spanish chapter is now 0.84–1.12 × its OG counterpart (OG words from the books
    DRSC-ES covers). The outlier is Post-apocalíptico at 0.68: the Carroñeo
    (scavenging) tables look shorter than OG's, a possible content gap to check in WP2,
    not a misplaced block.
  - 395,479 → 395,073 words; every removed word is accounted for (duplicate Posesión,
    Locura summary, the superhero power-boost intro, renamed headings, obsolete
    quick-reference entries).
- Verification run after each step:
  - same id set before and after, except intended aliases and new headings
  - 0 broken internal links; duplicate ids never increased (134 → 127 overall)
  - no duplicate id switched to a different target
  - balanced tags; word diff limited to headings, quick references and merged text
  - headless Chrome render of the moved sections
  The ODT and PDF are not updated (WP9).
- Acceptance: every DRSC-ES section sits under its OG chapter; no content lost
  (word-count and id diff against the pre-move baseline); anchor QA clean.

### WP2 — Gaps inside books already covered (~3k EN words + errata)
- [x] Heartwood (We Are All Mad Here), 2026-11-22, `wp2-gaps`:
      - the 6 descriptors as full entries in Cap. 15 (*Atormentado, Embrujado,
        Fragmentado, Frumioso, Perdido, Trocado*); the name-only list now links to them
      - the 6 foci in Cap. 6 (*Finge no tener miedo, Hizo un trato con la Muerte,
        Maldice al mundo, Muda de piel, Se hace amigo del perro negro, Vivió entre las
        hadas*), linked from the Heartwood foci list
      - the 4 Heartwood character arcs in Cap. 10 (*Convertirse en defensor, Desarrollar
        estrategias de afrontamiento, Echar raíces, Tomar el camino equivocado*) and a
        *Arcos de personaje de Heartwood* section in Cap. 15
      - fairy-tale skills: *Magia* was missing; *Empedrado* (paving) → *Zapatería*
        (cobbling, registered as `skill-cobbling`)
      - also fixed: the Cap. 10 sentence listing the arcs had link texts shifted from
        *Construcción* on (e.g. "Crecimiento" → `#creacion`)
      - not included: the Changeling NPC is from It's Only Magic (WP3). The Heartwood
        foci OG adds to the fantasy role suggestions came later, with all of OG's role
        additions (WP3, see there)
- [x] Diff existing rules text against CSRD 2025-08-22, 2026-11-22. **There are no
      errata to apply.** Compared the two CSRD files directly
      (`Cypher-System-Reference-Document-2023-04-18.docx` and `…-2025-08-22.docx`):
      every paragraph of the 2023 CSRD appears word for word in the 2025 one, except the
      title and one heading typo ("Exhorbitant" → "Exorbitant"). Everything new is in an
      appendix, "Additional rules and supplementary content from: The Stars Are Fire,
      Godforsaken, We Are All Mad Here, …, Neon Rain, and Cypher Shorts". For the books
      DRSC-ES covers, that new content is Heartwood (above); the rest belongs to the
      four supplements (WP3–6).
      - OG-CSRD's text is not always CSRD text. A first pass that diffed two OG
        versions found changes that are OG's own: *Secret and True Names* ("basic
        attacks, and Might defense"), the Giant Spider's venom (1 Speed damage instead
        of 3), the dropped note on *Efficacy Boost (Major)*, and the extra foci in the
        fantasy role suggestions. The CSRD keeps the original text in all four, as
        DRSC-ES does, so nothing was changed.
      - OG's "Errata" ability category keeps old 2015-Rulebook versions of renamed or
        changed abilities (e.g. Daring Escape → Misdirect) for compatibility. None of
        its 16 unmatched entries is in either CSRD: they are OG editorial (WP7).
      - OG also merges supplement text into core sections: Scavenging, Junk and the
        post-apocalyptic species intro (Rust and Redemption, WP6); Crafting Cyphers and
        the Masters Spells note (It's Only Magic, WP3); Character Reputations (Neon
        Rain, WP4).
- [x] Translate the missing abilities found by the WP0 audit: *Rayo de luna [Moonbeam]*
      and *Interrogar al yo pasado [Question Past Self]*, added to the ability list and
      their categories (2026-11-22). Neither is in the 2023 CSRD: the 2025 CSRD defines
      them inside It's Only Magic (the Practices Moon Magic focus and the Divination
      flavor). OG cites them with bare page numbers, which the audit reads as Rulebook
      pages. The text is verbatim CSRD 2025, so they stay; WP3 should not add them
      again. The 16 "errata" abilities are OG editorial (see above).
- [x] Fix five entries whose Spanish changed the range band (found by comparing range
      terms with OG-CSRD; see `GLOSARIO.md` › *Alcance y distancia*). Fixed in the HTML
      on 2026-11-22 (branch `wp2-gaps`) and registered in `CORRECCIONES.json` for the ODT:
      - *Reubicar [Relocate]*: the new position is *a largo alcance* (was *alcance
        inmediato*).
      - *Terremoto resonante [Resonant Quake]*: the epicentre is *a muy larga distancia*
        ("muy" was missing).
      - *Posthumano*: attacks *a muy larga distancia* ("muy" was missing).
      - *Vampiro*: garlic works *a una distancia inmediata* (was *corta distancia*).
      - *Mago poderoso*: affects creatures *a corto alcance del objetivo* (was *alcance
        inmediato*).
- [x] Normalise range/distance terminology across the text (2026-11-22, `wp2-gaps`;
      rules in `GLOSARIO.md` › *Alcance y distancia*). About 380 corrections:
      - 215 *distancia* → *alcance* where OG-CSRD says "range"
      - ~180 word-order fixes
      - 19 phrases that used *rango* (tier) for range
      Each was checked against the English of the same entry or paragraph, or reviewed
      by hand. The same pass removed two repeated, mistranslated sentences in *Niño mente
      colmena*. All are registered in `CORRECCIONES.json` and were applied to the ODT on
      2026-11-22 (WP9).
- Every text correction that also applies to the ODT goes into `CORRECCIONES.json`, and
  is applied to the HTML with `tools/fixes/apply_fixes.py --target html --record`.
- [x] Entries not found in OG and the Mutant descriptor (§3.4–3.6), 2026-11-22:
      - *Estabilizador mental [Mind Stabilizer]* is in OG as "Mind Stablizer" (Rulebook,
        page 393); keep.
      - *Mutant* is cited as Rust and Redemption, page 116 (WP6).
      - *Escudo deflector [Deflecting Shield]*: OG's editor's note says the deflecting
        shield (Godforsaken, page 150) "is not included in the CSRD"; both CSRD files
        list it by name only. **Decided 2026-11-22: keep** the Spanish entry (see §3.6).
- [x] Carroñeo vs OG Scavenging, 2026-11-22: *Carroñeo* is the 2023 CSRD Rulebook text
      and is complete. OG's Scavenging is Rust and Redemption's revised version (search
      time, doubled finds, Useful Stuff (Expanded), junk loads, its own Junk table),
      cited to both books, so the audit counts R&R words as covered; that explains the
      0.68 ratio. Port it with WP6.
- Acceptance: no OG section from ES-held sources without a Spanish equivalent.

### WP3 — It's Only Magic (~44k EN words) — done 2026-11-22
- [x] Ch14-A Magia moderna (character options, equipment, crafting ingredients,
      cyphers, artifacts). New Capítulo 12-A, before Ciencia ficción.
      - 67 cyphers plus EasyMagic.app and the malware cyphers note; 47 artifacts.
      - *Criaturas y PNJs de fantasía moderna por nivel* is OG's list (not in the CSRD).
        *Estatua animada* is listed at level 7, as in its entry (OG's list says 8).
- [x] 5 flavors (Ch6), 10 foci (Ch8), 7 descriptors, 125 abilities + cantrips (Ch9),
      Familiars and Covens (Ch11-A), equipment additions (Ch10).
      - Flavors in Cap. 4, foci in Cap. 6, descriptors in Cap. 12-A; 75 abilities in the
        Cap. 7 lists and 50 cantrips in *Trucos*.
      - Familiars and Covens done: *Familiares* and *Aquelarres* in Cap. 9-A, in OG's
        order (Sidekicks, WP7, will go between them). Coven rank is *círculo*. OG's
        editor's notes on Compañero bestia and the four familiar upgrades were added
        with them.
      - Reviving Artifacts done (the IOM equipment addition): *Regla opcional: Revivir
        artefactos* at the end of *Artefactos* in Cap. 8, with OG's editor's note, listed
        in the Cap. 8 and Magia moderna quick references and linked from the coven
        talisman note.
- [x] 13 creatures (Ch22), 4 NPCs (Ch23), including the Changeling NPC (*Trocado*).
      Inserted alphabetically into Criaturas and PNJs; the *Electricity Elemental* is its
      own entry next to the other elementals, as Criaturas already does.
- [x] Merged into core sections by OG: Crafting Cyphers (Godforsaken + IOM, page 90),
      the Masters Spells note about Inks Spells on Skin.
      - *Fabricación de objetos mágicos* (Cap. 11) now follows OG's merge: the
        *Habilidades de fabricación mágica* box, "materiales o ingredientes" in step 2,
        the IOM sentences and the Vanya examples in steps 3–5, and step 5 in the IOM
        wording. The Spanish keeps one heading per step. Three slips in the existing
        text were fixed through `CORRECCIONES.json` (`crafting-*`, plus
        `evil-priest-cypers`), pending for the ODT.
- Checked 2026-11-22: every It's Only Magic entry OG names (125 abilities and cantrips,
  foci, descriptors, cyphers, artifacts, creatures and NPCs) has a Spanish entry, matched
  by its English name; the source audit shows no IOM chapter left untranslated.

### WP4 — Neon Rain (~42k EN words)
- [x] Ch14-B Cyberpunk (cybernetics, dystopian society, drugs, technology, SHITS,
      hacking, netrunning, rules, cyphers, GM intrusions).
- [x] 9 foci, 5 descriptors, 49 abilities, Ch11 optional rules, Splitting XP (Ch12),
      Romance addition (Ch17).
      - 52 abilities done (OG counts Camera Sight and Drone Upgrade, which a first
        extraction missed). Machine Bond and Robot Builder have *(ciberpunk)* versions;
        Limited Camouflage has *(Técnico)* and *(sigilo)*.
      - 9 foci done (Cap. 6, with the ⚡ cyberware marker and GM intrusions as sidebars).
        New Capítulo 12-B *Ciberpunk* (nav, TOC, genres intro) with the 5 descriptors and
        *Rasgos de ciberpunk* (table, *Cambiar de rasgo*, additional foci, *Adaptar rasgos al
        ciberpunk*). OG's sidebar pointing to *Switching Character Options* is left out until
        that OG editorial section is translated (WP7).
      - Cap. 12-B *Ciberimplantes* (chrome, the three sample implants, ⚡ cyberware-derived
        abilities, armor, stat minimums, targeting and damaging cybernetics, salvaging) and
        *Tipos de ciberpunk* (Solo, As, Intermediario, Técnico, with the standard cyberpunk
        abilities) done. Type ability lists are sorted by Spanish name, as in Cap. 3.
      - Cap. 12-B setting sections done: *Sociedad distópica*, *Drogas*, *Tecnología
        ciberpunk*, *CAGADA*, *Hackeo*, *Netrunning*, *Reglas adicionales*, *Cyphers de
        ciberpunk*, *Intromisiones del DJ de ciberpunk* (categories in Spanish alphabetical
        order) and *Criaturas y PNJs de ciberpunk por nivel*.
      - Ch11 optional rules done: *Regla opcional: Daño definitivo* (box after *Daño*) and
        *Regla opcional: Persecuciones a alta velocidad* (box after *Situación especial:
        Persecución*, with OG's editor's note). The Cap. 9 quick reference gets a *Reglas
        opcionales* list with these two; OG's editorial optional rules join it in WP7.
      - Splitting XP done: *Regla opcional: Dividir los PX* (box after *Avance de rango en
        el Sistema Cypher*). The Cap. 10 quick reference gets a *Reglas opcionales* list
        (*Dividir los PX*, *Igualdad de avance*). OG's own Ch12 quick reference leaves
        Splitting XP out (it lists Slower Advancement twice).
      - Romance addition done: box *Reputación y relaciones de los personajes* (with
        *Usar los niveles de relación*) after the opening paragraphs of *Niveles de
        relación*, as in OG. The core paragraph "El nivel de las relaciones puede bajar o
        subir" moved into the box, where OG has it.
      - Linking pass done (2026-11-23): the 107 links recorded while Cap. 12-B was being
        written (from abilities, foci, descriptors and the chapter's own sections) now
        point at their Spanish sections. OG `choose-*` ids map to the section headings,
        not the quick-reference boxes. OG's broken `#cyberpunk-app-cyphers` link maps to
        *Comprar Cyphers de app*. Five links wait for WP7 sections (see WP7).

### WP5 — High Noon at Midnight (~38k EN words)
- [x] Ch21-A Oeste extraño (character options, currency, equipment, poker/hands of
      fate/deck as d20, showdown, curses, survival, tall tales, paranormal vices,
      threats/hazards, cyphers, artifacts).
- [x] 7 foci, 10 descriptors, 73 abilities, 11 creatures, 2 NPCs.
      - 76 abilities done (OG counts 67 new ones plus 9 High Noon versions of core abilities).
        The versions are named after their focus or vice, e.g. *Daño letal (Cobra recompensas)*
        and *Ojo certero (Ebrio)*. Cap. 7 gets a *Capacidades Q* section (*Que lo intenten*,
        *Quedar en tablas*).
      - 7 foci done (Cap. 6). OG's High Noon foci have no GM intrusions. New *Capítulo 19-A
        Oeste extraño* (nav, TOC, genres intro) with *Opciones de personaje* (OG's Dave Kehr
        quote, translated, with a link to the video instead of the embed), *Tipos sugeridos*
        (the types note drops its Daft Drafts part), *Rasgos del Oeste extraño* and the 9
        descriptors (OG has 9, not 10), including the *Forjado* and *Resucitado* species
        descriptors and *Avance de especie*. The Cap. 11 fantasy role suggestions now link
        the seven foci.
      - Cap. 19-A sections done: *Monedas*, *Equipo* (with *Recargar armas*), *Jugar al
        póquer*, *Manos del destino*, *La baraja como d20*, *Duelo*, *Maldiciones*,
        *Supervivencia*, *Historias increíbles*, *Vicios paranormales*, *Amenazas y peligros*,
        *Cyphers* (29 alchemical rounds and slugs) and *Artefactos* (22). Equipment rows,
        cyphers and artifacts are sorted by Spanish name; random tables keep OG's ranges.
      - 11 creatures (Cap. 20) and 2 NPCs (Cap. 21) done, inserted alphabetically. Cap. 19-A
        gets *Criaturas del Oeste extraño* (basic animals and NPCs, famosos, bestias malditas,
        forjados, pistoleros, necróvoros, with OG's stat lines) and the by-level table.
      - Linking pass done (2026-11-23): the 70 links recorded while Cap. 19-A was being
        written now point at their Spanish sections. OG ids that differ from their targets
        (`weird-west-necrovore`, `weird-west-gunslingers`, `creature-wraith`, the Ch25 heading)
        map through aliases. Five links wait: four for WP7 sections (see WP7) and one for
        WP6 (*Exposure*, see WP6).

### WP6 — Rust and Redemption (~36k EN words)
- [x] Ch19 Post-apocalíptico expansion (character options, equipment, optional rules,
      mutations, cyphers, artifacts). Cap. 18 now follows OG's h4/h5 order: equipment
      merged into one table set; *Reglas opcionales para el apocalipsis* (exposure,
      radiation, Carroñeo with basic and expanded Cosas útiles, Chatarra, Reparar y
      construir, Mantenimiento del equipo, advanced tech, incredible mutations); threats and
      GM intrusions; 23 cyphers; 4 pre-apocalyptic and 13 post-apocalyptic artifacts;
      *Criaturas y PNJs post-apocalípticos*; the QR with OG's sub-lists. The scavenging
      task table and "changing conditions" come from the CSRD (OG v2.11a lacks them).
- [x] Link from WP5: "un frío excesivo" in *Amenazas y peligros del Oeste extraño*
      (Cap. 19-A, Uncanny Blizzard) now points to *Exposición*.
- [x] 5 foci, 8 descriptors (including Mutant), 120 abilities + mutations list,
      15 creatures, 5 NPCs.
      - 19 regular abilities done (Cap. 7 lists). OG's *Know Where to Look* and R&R
        *Ruin Lore* entries are the core abilities word for word (*Saber dónde buscar*,
        *Conocimiento de ruinas*), so they get no new entry. The 100 mutations go in their
        own *Mutaciones* section at the end of Cap. 7, as in OG's Ch9.
      - *Mutaciones* done (Cap. 7, after *Trucos*): intro, *Regla opcional: Descriptor
        Mutante*, the beneficial, harmful, powerful, distinctive and cosmetic d100 tables, the
        crippling-mutations box and the 100 mutations in alphabetical order. Eight mutations
        whose Spanish name was already taken get *(mutación)*, e.g. *Telepatía (mutación)*.
      - 5 foci (Cap. 6) and 8 descriptors done. Cap. 18 now opens with *Opciones de personaje
        post-apocalípticas* as in OG: *Roles de personaje alternativos*, the existing types
        table (now an h5), *Rasgos post-apocalípticos* and *Descriptores post-apocalípticos*,
        with the species intro revised to R&R's wording and the existing Morlock and Roach
        moved in among the new descriptors (Spanish alphabetical order). The Cap. 11 role
        suggestions now link *Saquea*.
      - 15 creatures and 5 NPCs done. New h5 entries in Cap. 20 (*Ángel del Apocalipsis*,
        *Cuatro Jinetes del Apocalipsis* with *Bestia*, *Espada*, *Hambre* and *Peste* as
        h6, *Cucaracha brillante*, *Flor ganchuda*, *Fundido*, *Gusano gamma*, *Oso
        radiactivo*); h6 variants under existing entries, as OG does (*Zombi corredor*,
        *Zombi de IA*, *Zombi mastodonte* under *Zombi*; *Inteligencia artificial (IA)
        post-apocalíptica* under *Inteligencia artificial*; *Caníbal post-apocalíptico*
        under *Caníbal*); *Saqueador* in Cap. 21 with *Caudillo*, *Jinete despiadado* and
        *Merodeador*. The R&R *Blighted* template (*Plagado*) moves to WP7 with *Modifying
        Creatures*.
- [x] Revise Cap. 18 *Carroñeo* to R&R's Scavenging (Food, Water, and Shelter; Useful
      Stuff (Expanded); junk loads; Junk table), and the species-descriptor intro
      ("In addition to descriptors for human survivors…").
- [x] Linking pass: 37 of the 45 pending links applied. OG links the translation had dropped
      were restored: item links in the equipment tables and *Cosas útiles (ampliado)*,
      Vigor/Reserva/Armadura links in the exposure and radiation rules, and the Morlock
      descriptor's links. Inbound links from older sections were added (Chatarrero,
      Conocimiento de ruinas, Daño ambiental, Otros efectos), with OG's editor's note in
      *Especie como descriptor*. Per-section link counts now match OG, apart from the WP7
      links below.

### WP7 — OG editorial content (~68k EN words, prioritise per item)
- Decisions (2026-11-23): start with the OG sections that WP4–WP6 links wait for, then go
  chapter by chapter; leave out *What's in the Book*; Sidekick is *camarada*; keep omitting
  OG's source and page citations.
- [ ] Back matter: FAQ, Índice.
- [x] Ch1, Ch3, Ch4, Ch5 (2026-11-23). Decisions: Ch1 becomes *Acerca de esta edición* plus
      factual updates to the translator's notes; the generator, the checklist and the PDFs
      section are ported, with OG's character and sidekick sheets rebuilt in Spanish
      (`sheets/`, KUR-CSCS and KUR-CSSK) next to the existing KUR-CSQR; OG's online sheets list,
      its other PDFs and the product catalogues (*Additional Types*, and the Ch7/Ch8 ones) are
      left out; *¿Eres un jugador nuevo?* embeds a Spanish video chosen by the user.
      - Left for later: links in the new editor's notes to *An Example of Play* (Ch25), *XP
        Advance* (Ch12), OG's optional-rules index, *sixth-tier combat abilities* (ability
        categories) and three Errata abilities (*Shooting Gallery*, *Skills*, *Font of
        Inspiration*); the *campaign design checklist* link in the creation checklist.
- [x] Ch6 and Ch7 (2026-11-23): the two flavor optional rules (*Aspecto simplificado*,
      *Aspecto personalizado*) and OG's editor's notes in Cap. 4 and Cap. 5 (the *Especie como
      descriptor* and Descriptores-intro notes were added earlier). The flavor and descriptor
      catalogues from other products are left out.
      - Left for later: *optional character advancements* (Ch12), OG's optional-rules index
        (two more mentions) and the 2015 *Shipspeak* (Errata).
- [x] Ch8 (2026-11-23): the Cap. 6 quick reference gains all foci and suggested foci by genre;
      the focus-category quick reference gains *Personalización de los rasgos*, and the
      category intro list was repaired (two entries pointed at the wrong category); five
      editor's notes; *Rasgos psiónicos* (Cap. 13), missed in the first chunk. The foci
      catalogue from other products is left out.
      - When Ch16 Horror and Ch18 Superheroes are done, add their *Horror Foci* and *Superhero
        Foci* lists to the "Rasgos sugeridos por género" list in the Cap. 6 quick reference.
- [x] Ch9 (2026-11-23). Decisions: the Errata and OG-variant abilities are added to the A–Z list,
      tagged *(Errata)* or *(variante del OG-CSRD)*; OG's † and ‡ marks are kept, with their legend.
      - 25 entries: 19 old 2015-Rulebook abilities (16 with new names, plus the 2015 *Ligero de pies*,
        *Naveparlar* and *Lanzar*) and six OG variants (armor, shield, *Burlar*, *Lanzamiento
        rápido*). OG's Errata *Force Field* is the CSRD's current text, which *Campo de fuerza*
        already had; the 2019 wording is quoted in its editor's note.
      - Category lists rebuilt from OG's (1,137 → 1,702 items); Spanish-only items kept; plain
        text throughout (most lists were italic before, a few were not); a few cut-short labels
        fixed. Six new categories: *Acción extra*, *Atributos*, *Cyphers y artefactos*, *Errata*,
        *Recuperación*, *Tirada*.
      - The quick reference gains *Capacidades especiales*, *Activar una capacidad especial*, the
        legend, all categories with the three paranormal vices, the A–Z letters and the related
        sections DRSC-ES has.
      - 72 editor's notes and 9 sidebars added to the A–Z list. The other OG sidebars were already
        there, inline in parentheses as the CSRD prints them; the High Noon and Neon Rain notes
        were already on the book-version entries. Left out: OG's note on an English misprint in
        *Detect Life* and the immediate/close note on *Choque de energía* (the Spanish already
        says *alcance inmediato*).
      - Earlier WP7 notes now link *Galería de tiro*, *Habilidades*, *Fuente de inspiración*, the
        2015 *Naveparlar* and the combat aspect's sixth-tier list.
      - Left for later: *Calm Command*, *Hellfire* and *Icy Paths* in the Errata list (OG's own
        abilities in its Spacecraft and Power Shifts sections); links to OG's optional rule
        *Object Level, Health, and Armor* (*Weapon Properties* and *Alternative Armor
        Encumbrance* were linked in Ch10); the *Estrés* category and section, *Creating Cyphers, Artifacts, and Abilities*
        and *Sidekick Abilities* in the quick reference; *Skill Categories* and usage limits
        (Ch25) in two notes.
- [x] Ch10 (2026-11-23). Decision: the armor section keeps the CSRD paragraph and table; OG's
      clarified table (by experience, with prices), sidebar and worked example replace the
      translator's Twitter note, under an editor's note citing the 2024 Starter Set.
      - OG's five optional rules (*Dinero y agotamiento de recursos*, *Menor coste de Esfuerzo de
        Velocidad por llevar armadura*, *Carga de armadura alternativa*, *Armas letales*,
        *Propiedades de las armas*); *Armadura especial*; the priceless category (*invaluable*);
        OG's shield wording; three editor's notes and two sidebars; chapter quick reference
        expanded and a new *Artefactos* quick reference. The Daft Drafts note is left out.
      - The Ch9 links to *Carga de armadura alternativa* and *Propiedades de las armas* now resolve.
      - Five slips in the existing text fixed and recorded in `CORRECCIONES.json` (pending for the
        ODT).
- [x] Ch11 (2026-11-23): 13 of OG's optional rules plus *Ataques de área, Esfuerzo y daño*;
      *Así se juega al Sistema Cypher* as a heading and *El dial de dificultad*, which reuses the
      quick-reference dial SVG; 25 editor's notes; the driving sidebar in *Combate de vehículos*;
      hazards and crafting quick references; the chapter quick reference rebuilt with OG's groups.
      The CSRD text was already complete. The Ch9 links to *Nivel, salud y Armadura de los objetos*
      now resolve. Fixed "maniobrabi-lidad" (`CORRECCIONES.json`).
      - Left for later: links to Stress, Serious Injuries and Conditions, *An Example of Play*, the
        FAQ, OG's optional-rules index, *Making Meaning* and *Passive Difficulty*.
- [x] Ch11-A (2026-11-23): OG's *Seguidores frente a compañeros temporales* (with *Progresión de
      nivel de los seguidores* and *Equilibrar a los seguidores*), and Sidekicks as *Camaradas*
      (about 10k words): core rules with the sheet link (KUR-CSSK), the optional rules, 10 natures,
      10 niches, 10 fantastic niches with 19 templates and the mon-battle cyphers, and a catalog
      of 32 sidekick abilities. The CSRD followers, familiars and covens were already complete;
      OG's Daft Drafts note on covens is left out.
      - The sidekick sheet's provisional terms (*naturaleza*, *nicho*, *PJ asociado*) stay as they
        are. The Cap. 7 and *Modificar criaturas* quick references now link *Capacidades de los
        camaradas*.
      - Left for later: OG's *Power Shifts in Other Genres* (two links).
- [x] Sidekicks (Ch11-A, ~10k). Done in Ch11-A (2026-11-23) as *Camaradas*.
- [x] Ch12 (2026-11-23): OG's four optional rules (*Adelanto de PX* with its benefits and
      complications tables, *Empezar en rango 0* with *Avanzar a rango 1*, *Avance más lento*,
      *Avanzar más allá del rango 6*), placed with *Dividir los PX* in one box as OG does, and
      *Avances de personaje opcionales*; four editor's notes (*Otras opciones*, rerolls and GM
      intrusions, covens, romance); the CSRD's second paragraph in the sample-arcs sidebar; the
      chapter quick reference gains OG's optional rules, related sections and the *Gastar 1/2/3/4/10
      PX* lists. The GM intrusion sidebar now names and links Cap. 23. The CSRD's "about half their
      XP from arcs" sidebar is already inline in parentheses, so it is not repeated.
      - The links to *XP Advance* (Cap. 2, Cap. 3) and *Optional Character Advancements* (Cap. 4)
        now resolve; the existing text said *avance de PX*, now *adelanto de PX*.
      - Left for later: OG's *Separate Reroll and GM Intrusion Refusal Costs* (Ch25), Psionics and
        Posthuman Upgrades (OG-only, from the Science Fiction book), *Extended Vehicular Combat*,
        Stress, Serious Injuries and Conditions, *Skill Categories* and OG's optional-rules index.
- [x] Ch13 (2026-11-23): OG's *Asignar límites distintos a las capacidades sobrenaturales* (about
      900 words, two tables) after the spellcasting rule; the chapter quick reference rebuilt with OG's
      groups, the spellcasting one expanded, and new ritual magic, fantasy equipment and traps quick
      references; seven editor's notes (new foci, cyphers as spells, tier categories, cultivation
      fantasy, *Operación peligrosa*, coinage, the Frozen Timepiece); OG's armor fix (full plate 2,
      scale 3) with its note.
      - Structure: *Luchador* gets its own heading (it was a paragraph inside *Druida*); the
        character options and their quick reference are in alphabetical order; *Tecnología mágica*,
        *Nombres secretos y verdaderos* and *Deseos* move under *Módulo de reglas de fantasía* as in
        OG; the five example artifacts join the A–Z artifact list, and the artifact and cypher lists
        are re-sorted. Two capitalisation slips fixed (`CORRECCIONES.json`).
      - The CSRD sidebars (trap intrusions, ritual notes, *Dianxue*, etc.) were already inline. The
        minor artifacts table keeps *Escudo deflector*, which DRSC-ES has, so OG's notes on replacing
        it are left out, as are the 14 Daft Drafts notes and the *Wizards and the Optional
        Spellcasting Rule* title note (DRSC-ES already has that heading).
      - Left as is: the short *Criaturas y PNJs básicos* list followed by the full *Otras criaturas y
        PNJs* list (OG has only the full one); a WP8 candidate.
      - Left for later: *Power Shifts in Other Genres*, Psionics, *Creating Cyphers, Artifacts, and
        Abilities*, Stress (three links) and Serious Injuries and Conditions.
- [x] Ch14 (2026-11-23). Decision: OG's price tables replace the CSRD ones. The CSRD tables
      disagree with the CSRD's own contemporary item entries (hand grenade 4 vs 6 damage, sports car
      exorbitant vs very expensive, cell phone and handcuffs vs Smartphone and Restraint); OG rebuilt
      them from the entries and added *Artículos invaluables*. Only the concealed microphone and the
      luxury car rows are gone.
      - An editor's note explains the rebuild and carries OG's notes on "contemporary" equipment,
        tech levels and variable prices; OG's hand grenade note; the chapter and equipment quick
        references rebuilt with OG's groups; basic creatures sorted.
      - Already there: the mundane foci list and its adjustments table, the three CSRD sidebars.
        The contemporary items stay in level order, as in the CSRD.
- [x] Ch14-A (2026-11-23): Cap. 12-A was translated from OG in WP3 and matches it (126 entries,
      67 cyphers, 47 artifacts, the six descriptor errata notes, the cypher-limit note, the
      sidebars). Only the quick reference changed: OG's descriptor group and *Oeste extraño* among
      the related sections. OG's Daft Drafts note stays out.
- [x] Links left from WP4, WP5 and WP6, now resolved (2026-11-23, see below); the sections they waited for:
      - *Creating Challenging Encounters* (Ch25): "daño duradero y daño permanente" in
        *Daño duradero y permanente*, "daño duradero" in *Regla opcional: Tiempo de
        inactividad forzoso* and in *Intromisiones de salud* (Cap. 12-B).
      - *Optional Rule: Choosing a Combat Effect Ahead of Time* (Ch11): "eliges un efecto
        de combate de antemano" in *Atacar los ciberimplantes* and "elegir un efecto de
        combate de antemano" in *Dañar los ciberimplantes* (Cap. 12-B).
      - *Switching Character Options*: OG's sidebar in *Rasgos de ciberpunk* that points
        to it was left out; add it with the section.
      - *Creating Challenging Encounters* (WP5): "daño duradero" in the *Forjado* descriptor
        (Cap. 19-A).
      - *Celebrity* creature template and *Modifying Creatures* (Ch25): "famosos", "Famoso"
        and "Modificar criaturas" in *Famosos* (Cap. 19-A).
      - *Blighted* creature template (R&R, in OG's *Modifying Creatures*): translate it as
        *Plagado*, then link the *Plagado* mentions in Cap. 18 (*Criaturas, plantas y PNJs
        mutados*, *Criaturas y PNJs post-apocalípticos*) and "plantillas de criatura" there.
      - Links left from WP6 (WP6 `pending-links.json`): OG's *Mundane Foci*, *Fantasy Foci*
        and *Science Fiction Foci* lists ("rasgos mundanos", "rasgos de fantasía", "rasgos de
        ciencia ficción" in *Rasgos post-apocalípticos*, Cap. 18); *Optional Rule:
        Transferring Subtle Cyphers* ("transferir Cyphers sutiles" in *Cyphers sutiles de
        carroñero*); *Plagado* in *Apocalipsis nuclear*.
      - Done (2026-11-23): Cap. 23 *Modificar criaturas* (templates *Reforzado*, *Más grande y
        resistente* moved from Cap. 20, *Plagado*, *Famoso*), *Esfuerzo para PNJs*, *Criaturas con
        varias partes*, *Crear criaturas y PNJs*, *Crear encuentros desafiantes*; Cap. 9 *Elegir
        un efecto de combate de antemano*; Cap. 22 *Transferir Cyphers sutiles*; Cap. 2 *Cambiar
        las opciones de personaje* (plus OG's links to it and its Descriptores editor's note);
        *Rasgos de fantasía*, *Rasgos mundanos*, *Rasgos de ciencia ficción*. OG's "This section
        is based on…" source lines are omitted like the page citations.
      - Left for later WP7 items: "Estrés" and "heridas graves y condiciones" in *Crear
        encuentros desafiantes* (Stress and Serious Injuries); the "Sidekick Abilities" entry in
        the *Modificar criaturas* quick reference (Sidekicks).
- [ ] Running the game additions (Ch25, ~14k): campaign design checklist, session
      preparation, teaching the rules, making meaning, example of play.
- [ ] Stress and Serious Injuries (Ch16, ~4k), ~46 OG optional rules, editor notes,
      "Related Sections", page citations (decide whether to keep OG page numbers or map to
      Spanish/CSRD pages).
- [x] Errata ability category (old 2015-Rulebook versions, 16 entries without a
      Spanish match). Done in Ch9 (2026-11-23).
- [x] Book abilities in the Cap. 7 category lists: OG's *Abilities by Category* lists
      include It's Only Magic, Neon Rain, High Noon at Midnight and Rust and Redemption
      abilities (about 613 of 1,494 unique entries); the Spanish lists still have only the
      core abilities. Found in the WP6 verification (2026-11-23). Done in Ch9 (2026-11-23).
- [ ] Typo in Cap. 15 Cuentos de hadas (on main before WP6): "nivel 7 para Defensa de debido a su
      intangibilidad" is missing the stat.
- [x] Expanded fantasy role suggestions (Cap. 11), done early in WP3 (2026-11-22):
      OG's added foci, flavors and specialisations, the Artífice o erudito and Psiónico
      roles, and their editor's notes. When WP5 and WP6 translate High Noon at Midnight
      and Rust and Redemption, link their foci in these roles (provisional names in
      `GLOSARIO.md`).
- [x] Optional Rule: Exceeding Cypher Limits (Ch24), done early in WP3 (2026-11-22):
      *Regla opcional: Superar el límite de Cyphers* in Cap. 22 under *Límites de
      Cyphers*, with the *Volatilidad de los Cyphers* table and OG's note pointing to
      Magia moderna; the Magia moderna note now links back to it.
- OG additions are not labelled in the text (§2); editor's notes keep *Nota del editor:*.

### WP8 — Structural integration (incremental, alongside WP1–WP7)
- [ ] Renumber/reorder to the target structure in §4.
- [ ] Update TOC and both navbar dropdowns.
- [ ] Extend part-colour theming and quick-reference styling to new content.
- [ ] Fix the 134 pre-existing duplicate ids and normalise new ids.
- [ ] Preserve the ES-only appendix.
- Acceptance: navigation complete; no orphan sections; anchors coherent.

### WP9 — QA and release
- [ ] Run anchor/duplicate/structure checks (expect 0 missing anchors, no new dupes).
- [ ] Headless render in light and dark; confirm no console errors.
- [ ] Link sweep and cross-reference audit; re-run the §3 source audit.
- [ ] Proofread pass against the glossary.
- [ ] ODT and PDF: the ODT keeps its current structure (the WP1 reorganisation is not
      ported to it) and only gets the text corrections registered in `CORRECCIONES.json`.
      - Apply them with `tools/fixes/apply_fixes.py --target odt --record`; it matches
        text across the ODT's `<text:span>` splits.
      - Then regenerate the PDF, exported untagged.
      - Keep "Hyphenate last word" enabled in the ODT; disabling it crashes LibreOffice
        26.8 (tdf#173973).
      - [x] 2026-11-22 (branch `wp2-gaps`): the 386 corrections registered so far
            applied; PDF regenerated with LibreOffice 26.8.3.1 (544 pages, untagged, same
            links and bookmarks as before). Repeat for corrections added later.
      - [x] 2026-11-22: `skill-cobbling` applied (*Zapatería*) and the fairy-tale skills
            table re-sorted; PDF regenerated (544 pages, same links and bookmarks; only
            page 351 changed). The ODT already had *Magia*; only the HTML lacked it.
      - The first ODT run showed that the applier could empty a link, or keep an ODT
        space element, when a correction crossed markup. The applier now aligns
        changes word by word and checks the result. The one link affected in the HTML
        (*Arremetida* in Cap. 1 › *Alcance y velocidad*) was restored.
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
- When moving a section, move its HTML block intact (heading, id, anchor, body) and
  fix only the heading level and surrounding quick references.

---

## 7. Terminology governance

- Maintain `GLOSARIO.md` with one canonical Spanish term per English term.
- Follow existing choices from the translation notes (e.g., Cypher=Cypher,
  ease=aliviar, hinder=obstaculizar, round=ronda, trained=competente,
  specialized=especialista, tier=rango, level=nivel).
- Flag conflicts early; do not silently vary terms across chapters.

---

## 8. QA and verification

Automated checks to run after each work package (see `tools/README.md`):

1. Internal anchors: every `href="#x"` resolves to an `id="x"`
   (`tools/qa/check_html.py`).
2. Duplicate ids: no new duplicates, and no duplicated id may switch to a different
   target element (`check_html.py --baseline <branch point>`); drive the remaining 127 to
   zero in WP8.
3. HTML structure: balanced tags, no unclosed containers (`check_html.py`).
4. Render: load in headless Chrome in light and dark, assert no console errors, spot
   check tables, sidebars, quick refs, tabbed items and dropdowns
   (`tools/qa/render.py --section ID`).
5. Coverage: re-run the source-attribution audit (`tools/parity/audit.py`, §3.1); every
   named entry should sit in its OG chapter, and the missing-entry list should shrink.
6. Glossary: `tools/parity/glossary.py --check` after adding or renaming entries.

---

## 9. Milestones and sequencing

| Milestone | Content | Depends on |
|---|---|---|
| M1 | Existing content reorganised to OG structure (WP1) | WP0 |
| M2 | Gaps inside covered books closed: Heartwood, CSRD 2025 errata (WP2) | M1 |
| M3 | It's Only Magic (WP3) | M1 |
| M4 | Neon Rain (WP4) | M1 |
| M5 | High Noon at Midnight (WP5) | M1 |
| M6 | Rust and Redemption (WP6) | M1 |
| M7 | OG editorial content (WP7) | M1 |
| M8 | Structural integration + full QA, ODT/PDF sync (WP8–WP9) | M1–M7 |

Recommended order: WP0 → WP1 → WP2 → WP3–WP6 (any order; parallelisable by book) →
WP7 → WP9, with WP8 integrated incrementally to keep anchors and navigation
consistent. Doing WP1 first means every later addition goes straight into its final
place.

---

## 10. Effort estimate

- Reorganisation (WP1): ~4–8 days, no translation.
- Translation volume:
  - Core (WP2–WP6): ~162k EN words → ~180k Spanish words, about 65–110 person-days.
  - OG editorial (WP7): ~68k EN words, about 27–45 person-days. Index and What's in
    the Book are mostly generated lists and go faster.
- Throughput: ~1,500–2,500 words/day for prose; slower for stat blocks and
  link-heavy lists.
- Total: **~75–130 person-days** for the core, **~100–175** including all OG
  editorial content, for one translator/editor. Parallelisable by source book.
- Calendar: core roughly 4–6.5 months at ~20 working days/month for one person;
  faster with a small team split by book.

---

## 11. Risks and mitigations

| Risk | Mitigation |
|---|---|
| OG editorial rulings diverge from official CSRD | Keep official rules wording; OG's notes keep the *Nota del editor:* label |
| Terminology drift across hundreds of entries | `GLOSARIO.md` + review gate per milestone |
| Duplicate/broken ids while adding hundreds of entries | Automated id/anchor checks each WP; fix pre-existing dupes |
| Losing ES-only or existing content during reorganisation | Move blocks intact; diff ids and word counts against the pre-move baseline |
| Inbound links to moved sections break | Keep ids on moved sections; alias anchors where sections merge |
| ODT/PDF drift from the HTML | The ODT gets only the corrections in `CORRECCIONES.json` (applied with `tools/fixes/apply_fixes.py`); keep the LibreOffice crash workaround (tdf#173973) |
| File size/performance growth (~4 MB → 6–7 MB) | Monitor load time; consider section splitting if needed |
| Scope creep (OG tools/randomizer/tooltips) | Use the definition of done; treat tools as WP7 items |

---

## 12. Immediate next actions

1. Merge `wp1-fantasy-relocation`, then `wp0-setup` (both complete).
2. Settle the two open terminology decisions in `GLOSARIO.md` ("training", *Aspecto*)
   and normalise the existing text to them. Range/distance is already normalised.
3. WP2 (branch `wp2-gaps`): close the Heartwood gap, add the 18 missing abilities and
   check Carroñeo. The five range-band errors are already fixed.
4. Pick the first supplement for WP3–WP6 and translate it in one pass.
