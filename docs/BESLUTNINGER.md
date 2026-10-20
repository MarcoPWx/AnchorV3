# Beslutninger

Én række pr. beslutning. **Status:** BESLUTTET (operatøren har sagt ja), RETNING (operatørens udtrykte retning,
bekræftes ved review af denne PR), ÅBEN (venter). Nye beslutninger tilføjes nederst; en ændret beslutning får en
ny række, der peger på den gamle. Kilde for alle: samtale med operatøren 2026-10-20 og målinger samme dag.

| ID | Beslutning | Status | Hvorfor / evidens |
|---|---|---|---|
| B-001 | **Nyt repo, start tomt, alt via PR.** V2 forbliver reference og historik | BESLUTTET | Operatøren: "vi starter fra en frisk med fuld kontrol og PR's". Løser roadmappens K1 (kodehjem) |
| B-002 | **TUI-først. Desktop-appen droppes.** | RETNING | Operatøren: "tror ikke folk gider downloade en desktop app". Måling: kun ca. 4 % af desktop-appens ca. 16.200 linjer kunne genbruges direkte |
| B-003 | **Navne: Anchor** (TUI-arbejdsfladen) og **Anchor Atlas** (manual og læring, HTML fra samme register). Læring er slået til som standard og kan slås fra | BESLUTTET | Operatørens valg |
| B-004 | **Værktøjsroller:** Linear = opgaver og status · Sketch = tegnebræt for design-hensigt · Git = kode og register · Kæden = hændelser. Status bor aldrig to steder | RETNING | "Hvor bor viden"-princippet. Sketch er ikke under git: en arkitektur-PR eksporterer berørte rammer som SVG |
| B-005 | **Kerne med kontrakter + tynde adaptere** (CLI, API, MCP, TUI). V2's `cli.py` porteres ikke | BESLUTTET af planen | Målt: `cli.py` 12.631 linjer; 58 cli-filer = 19.925 linjer; `serve/__init__.py` 7.000 linjer; 115 `anchor.*.vN`-skemaer spredt. Kun grønne, brugte kommandoer kommer ind (CLI-registret: 123 grøn, 106 gul, 139 rød, 11 ikke kørt af 379) |
| B-006 | **API: FastAPI med kontrakter som modeller** er kandidat | ÅBEN | V2 bruger Pythons indbyggede `http.server`, skrevet i hånden (`serve/__init__.py:73`) |
| B-007 | **Lagring:** kæden er sandhed for hændelser; DuckDB er et *afledt* lager, der kan genbygges; embeddings/RAG udskydes | RETNING | Se [DATA.md](DATA.md) |
| B-008 | **Signaler kører async:** producere på kadence (nysgerrighed, devil's advocate, fejlmønstre) → kø → vises på beslutningstidspunktet (højst tre) → lukkes med én tast (HIL) → præcision måles pr. signaltype | RETNING | Hooks, der arbejder inline, bliver annulleret af værten (PreCompact og Stop, ANC3-10). DA har 1.990 åbne udfordringer: skrevet, ikke lukket |
| B-009 | **Køen opsamler steering.** `anchor steer "idé"` lægger idéen i køen; den aktuelle opgave fortsætter; køen sorteres ved checkpoint (SHIP/DEFER/KILL). Køen ved, *hvem* der steerer | RETNING | Operatøren: "en smart måde at orchestrere arbejde, hvis man har mange idéer". Kendt fejl: steer-capture fejllæste beskeder fra andre sessioner to gange |
| B-010 | **INIT danner overblikket og TUI'en guider dig igennem det** (rundtur med HIL-spørgsmål); kortet kan eksporteres til Sketch som genererede rammer | RETNING | Operatøren: "init fasen skal kunne danne et overblik … og guide dig gennem TUI". Basislinje at slå: håndkørt INIT med 48 agenter, ca. 10,2 mio. tokens, ca. 2 t 20 min |
| B-011 | **GenAI Academy hører ikke til i V3** (flyttes til CertQuest eller arkiveres) | ÅBEN | Operatøren: "lever bedre sammen med CertQuest". Afgøres af en måling af, hvad der bruges |
| B-012 | **Om Anchor hjælper, afgøres af et forhåndsregistreret forsøg** (CertQuest, kørt af Codex, parrede arme, uafhængig bedømmer) | RETNING | Operatøren: "meget vigtigt at denne test er scientific" |
| B-013 | **Alt er versioneret og sporbart, ned til mindste beslutning.** Hvert begreb, hver fakta og hver beslutning har id, version, dato og kilde og linker på tværs: kæde-id, git-sha, Linear-id, Sketch-UUID og draw-id. Anchor Atlas får en **versionsvælger**, så man kan se et begreb, som det så ud på en given dato | RETNING | Operatøren: "ALT, ned til mindste beslutning, er versioneret og traceable across alle knowledge graphs". V2-registret har allerede versioner og trin pr. begreb (`concepts.py`), men 24 af 49 versioner manglede spor |
| B-014 | **Atlas = versionerede ADR'er og kontrakter; alt udviklingsarbejde er i TUI'en.** Atlas ændres kun når en PR ændrer en ADR eller en kontrakt, og så skifter versionen (fx SCDD-kontrakten 0.1 → 0.2). Atlas genereres fra repoet ved merge, så ingen vedligeholder det i hånden. TUI'en viser alt levende: opgaver, fremdrift, målinger, HIL, køen og signaler, og linker til Atlas-siden for den kontraktversion, der gælder (`scdd@0.2`). Regel: Atlas viser aldrig et tal, der kan ældes, medmindre det er en del af en kontraktversion; TUI'en indeholder aldrig definitioner | BESLUTTET | Operatøren: "Vi bruger meget energi på at holde atlas opdateret … atlas er kun til nye ADR og fx kontrakten til SCDD er nu 0.1, laver vi en ændring og PR er det 0.2". Erstatter den del af B-003, der lagde læring og levende fakta i samme side |

## Åbne fra den flettede roadmap

K2 roller · K3 dækningsenhed · K4 forrangs-ADR · K5 første vært · K6 frys fixtures · K7 forhåndsregistrering og
modelforbrug · K8 pilot-betydning · K9 koordinering af flere skrivere · K10 læreflade (= Anchor Atlas, B-003) ·
K11 planautoritet. Se Linear-dokumentet for detaljer.
