# Plan for Full Parity: DRSC-ES → OG-CSRD

Status: in execution. WP1 is in progress on branch `wp1-fantasy-relocation`; see
the WP1 checklist in §5 (last updated 2026-11-22). The plan was revised on 2026-11-22
after a source-attribution audit (§3).
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
- **Terminology:** reuse the existing DRSC-ES glossary; keep English names in
  `[brackets]` exactly as the current document does.
- **Editorial policy:** full parity includes OG editorial content (foreword, editor
  notes, page citations, "Related Sections", Index, FAQ, What's in the Book,
  Character Sentence Generator, PDFs/Player's Guide links). Where OG makes an
  editorial ruling that differs from the official CSRD, preserve the official rules
  wording and mark the OG addition as such (a Spanish equivalent of the OG badge).

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
| Cap. 15 Cuentos de hadas › Bestias y seres (~15.9k) | Fairy-tale stat blocks | Ch22 / Ch23 (Ch20 keeps the Beasts and Beings overview: magical animals, talking objects, beings by archetype) | Done (inline beings, archetype lists and PNJs intro stay in Cap. 15; Hada and Bruja pairs still to merge, §3.6) |
| Cap. 20 Criaturas › Supervillanos (~2.7k) and NPC entries filed as creatures | Supervillains, NPCs | Ch23 NPCs (Ch18 keeps the Supervillains overview) | Done (Supervillanos moved whole, after Otros PNJs) |

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
  2023-04-18 and 2025-08-22 (Rulebook 2024 errata). A structural audit cannot detect
  these. OG's "Errata" ability category is a starting list.
- **Mutant descriptor** (post-apocalyptic). OG gives no citation; it sits among the
  Rust and Redemption descriptors. Verify its source.

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
- Not found in OG under any name; check against CSRD 2025 before keeping or removing:
  - *Estabilizador mental [Mind Stabilizer]* (cypher, Cap. 22)
  - *Escudo deflector [Deflecting Shield]* (fantasy artifact, Cap. 23)
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
  - Duplicate ids are down from 134 to 128.
- Decided: keep both *Sátiro* entries (Godforsaken and We Are All Mad Here), each
  identified by origin; the fairy-tale one is labelled *(Cuentos de hadas)*.
- Still open:
  - *Hada* / *Hada (Cuentos de hadas)* and *Bruja* / *Bruja (Cuentos de hadas)* sit next
    to each other in Criaturas/PNJs. They are the same creature at the same level but
    written differently (different description, environment and abilities); OG merges
    each pair into one listing. Decide whether to merge them or keep both.
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

### WP0 — Setup (0.5–1 day)
- [ ] Record the locked source version in the document header.
- [ ] Create `GLOSARIO.md` (EN→ES term map) and `TRADUCCION-PROGRESO.md`
      (per-section status).
- [ ] Add QA scripts: anchor target check, duplicate-id check, HTML structure check,
      headless render (light/dark).
- [ ] Add the source-attribution audit (OG `og-cite` per section + ES bracket-name
      matching) so §3 can be re-run after each work package.

### WP1 — Reorganise existing Spanish content (no new translation, ~4–8 days) — relocations done; two duplicate pairs open
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
- [x] Sort Criaturas and PNJs ignoring a leading El/La/Los/Las; keep both Sátiro
      entries, labelled by origin.
- [ ] Decide and apply the Hada and Bruja merges (§3.6).
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
- Verification run after each step:
  - same id set before and after, except intended aliases and new headings
  - 0 broken internal links; duplicate ids never increased (134 → 128 overall)
  - no duplicate id switched to a different target
  - balanced tags; word diff limited to headings, quick references and merged text
  - headless Chrome render of the moved sections
  The ODT and PDF are not updated (WP9).
- Acceptance: every DRSC-ES section sits under its OG chapter; no content lost
  (word-count and id diff against the pre-move baseline); anchor QA clean.

### WP2 — Gaps inside books already covered (~3k EN words + errata)
- [ ] Translate the 6 Heartwood descriptors and 6 Heartwood foci (We Are All Mad Here)
      and replace the name-only lists.
- [ ] Diff existing rules text against CSRD 2025-08-22 and apply errata (start from
      OG's "Errata" ability category).
- [ ] Resolve the two entries not found in OG and the Mutant descriptor source (§3.4–3.6).
- Acceptance: no OG section from ES-held sources without a Spanish equivalent.

### WP3 — It's Only Magic (~44k EN words)
- [ ] Ch14-A Magia moderna (character options, equipment, crafting ingredients,
      cyphers, artifacts).
- [ ] 5 flavors (Ch6), 10 foci (Ch8), 7 descriptors, 125 abilities + cantrips (Ch9),
      Familiars and Covens (Ch11-A), equipment additions (Ch10).
- [ ] 13 creatures (Ch22), 4 NPCs (Ch23).

### WP4 — Neon Rain (~42k EN words)
- [ ] Ch14-B Cyberpunk (cybernetics, dystopian society, drugs, technology, SHITS,
      hacking, netrunning, rules, cyphers, GM intrusions).
- [ ] 9 foci, 5 descriptors, 49 abilities, Ch11 optional rules, Splitting XP (Ch12),
      Romance addition (Ch17).

### WP5 — High Noon at Midnight (~38k EN words)
- [ ] Ch21-A Oeste extraño (character options, currency, equipment, poker/hands of
      fate/deck as d20, showdown, curses, survival, tall tales, paranormal vices,
      threats/hazards, cyphers, artifacts).
- [ ] 7 foci, 10 descriptors, 73 abilities, 11 creatures, 2 NPCs.

### WP6 — Rust and Redemption (~36k EN words)
- [ ] Ch19 Post-apocalíptico expansion (character options, equipment, optional rules,
      mutations, cyphers, artifacts).
- [ ] 5 foci, 8 descriptors, 120 abilities + mutations list, 15 creatures, 5 NPCs.

### WP7 — OG editorial content (~68k EN words, prioritise per item)
- [ ] Back matter: FAQ, Índice, Qué hay en el libro, Prólogo.
- [ ] Character tools: Character Sentence Generator, creation checklist, PDFs links.
- [ ] Sidekicks (Ch11-A, ~10k).
- [ ] Running the game additions (Ch25, ~14k): campaign design checklist, session
      preparation, teaching the rules, making meaning, example of play.
- [ ] Stress and Serious Injuries (Ch16, ~4k), ~46 OG optional rules, extra ability
      categories, editor notes, "Related Sections", page citations (decide whether
      to keep OG page numbers or map to Spanish/CSRD pages).
- [ ] Mark every item as an OG addition per §2.

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
- [ ] Bring the ODT and PDF in line with the HTML. Keep "Hyphenate last word" enabled
      in the ODT; disabling it crashes LibreOffice 26.8 (tdf#173973). Export the
      PDF untagged.
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

Automated checks to run after each work package (scripts already prototyped):

1. Internal anchors: every `href="#x"` resolves to an `id="x"`.
2. Duplicate ids: no new duplicates; drive the pre-existing 134 to zero.
3. HTML structure: balanced tags, no unclosed containers.
4. Render: load in headless Chromium (light and dark), assert no page errors, spot
   check tables, sidebars, quick refs, tabbed items and dropdowns.
5. Coverage: re-run the source-attribution audit (§3.1); every OG section should map
   to a DRSC-ES section in the same chapter.

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
| OG editorial rulings diverge from official CSRD | Keep official rules wording; mark OG additions explicitly |
| Terminology drift across hundreds of entries | `GLOSARIO.md` + review gate per milestone |
| Duplicate/broken ids while adding hundreds of entries | Automated id/anchor checks each WP; fix pre-existing dupes |
| Losing ES-only or existing content during reorganisation | Move blocks intact; diff ids and word counts against the pre-move baseline |
| Inbound links to moved sections break | Keep ids on moved sections; alias anchors where sections merge |
| ODT/PDF drift from the HTML | Sync in WP9; keep the LibreOffice crash workaround (tdf#173973) |
| File size/performance growth (~4 MB → 6–7 MB) | Monitor load time; consider section splitting if needed |
| Scope creep (OG tools/randomizer/tooltips) | Use the definition of done; treat tools as WP7 items |

---

## 12. Immediate next actions

1. Finish WP1: decide the Hada and Bruja merges (§3.6), then merge
   `wp1-fantasy-relocation`.
2. Create `GLOSARIO.md` and `TRADUCCION-PROGRESO.md`.
3. Add the QA scripts and the source-attribution audit to the repo (read-only checks):
   id-set diff, link resolution, word diff and tag balance, as used in WP1.
4. Close the Heartwood gap (WP2), a small self-contained task.
5. Pick the first supplement for WP3–WP6 and translate it in one pass.
