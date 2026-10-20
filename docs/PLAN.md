# Plan: de første PR'er

Hver PR er ét begreb eller én bid fra roadmappen ([Linear](https://linear.app/anchored/document/v3-roadmap-flettet-20-okt-laesemaskinen-bid-for-bid-20-bidder-0daff2acfe61)),
med tests først, oprindelse fra V2 (`sti @ sha`) og en opdateret atlas-række. Rækkefølgen kan ændres af
resultaterne nedenfor under "Venter på".

| PR | Indhold | Bid | Færdig når |
|---|---|---|---|
| 0 | **Grundlag**: README, AGENTS.md, beslutninger, plan, data (denne PR) | — | Operatøren har læst og godkendt |
| 1 | **Skelet + atlas-værktøj**: mappestruktur, registret og `concepts.py` med tests fra V2 (`packages/anchor/docs/learning/concepts-2026-10-20/tools/` @ `054a6989c`), CI der kører testene | 0 (afstem først) | 18 tests grønne i CI |
| 2 | **Data-inventar**: målt oversigt over V2's data (kædens 78 event-typer, TSV, JSONL, DuckDB, commits) som registerfakta med dato og kilde. Ingen data kopieres | 3 | Hver tal kan genmåles med en kommando i PR'en |
| 3 | **Streng projektbinding** i kernen: præcis ét projekt eller en navngiven afvisning; kontrakt + tests | 2 | RED → GREEN; aldrig fald tilbage til Anchors eget projekt |
| 4 | **Inventar** (INIT tæller et repo): kind, enhed og nævner pr. kilde; TypeScript tælles som ulæst, ikke som nul; repo uden docs = NO_DOCS, ikke 0,0 | 3 | Kører på en kopi af CertQuest med tal, der kan genmåles |
| 5 | **TUI-rundtur v0**: læser registret, viser kortet og trinnene; HIL-svar gemmes gennem kernen | 14 (spørgsmål) | Operatøren kan gå rundturen på V2-repoet |
| 6 | **Range-ledger**: hvad er læst, af hvilken revision, hvor fortsætter jeg | 4 | Genskaber tallet 3,2 % for V2 |

**Første demo:** INIT-rundturen i TUI'en, først på Anchor V2-repoet, så på en kopi af CertQuest.

**INIT's første testkorpus er V2's egen `docs/`:** research-pakkerne (26.945 filer i 267 pakker, målt
2026-10-20), datapits og TSV-filerne. Vi bygger INIT stille og roligt og forventer at finde meget mere,
end vi kender i dag. Hvert fund bliver et begreb på trinnet "Opdaget", og operatøren vælger via HIL, hvad
der bliver til noget. Det er samme sløjfe, der fandt 8 nye begreber i Sketch-dokumentet 2026-10-20.

## Arkitektur i én linje pr. lag

- **Kerne:** funktioner med kontrakter (ét skema-katalog, ikke 115 spredte). Ingen I/O-logik i adaptere.
- **Adaptere:** CLI (tynd, en kommando ≈ få linjer), API (FastAPI-kandidat, B-006), MCP (læseværktøjer), TUI (Textual).
- **Baggrund:** producere på kadence skriver til en kø eller sidecar; ingen tungt arbejde i hooks (B-008).
- **Lagring:** se [DATA.md](DATA.md).

## Venter på (resultater fra 2026-10-20)

- "Har vi brug for det?"-tabellen for maskinrummet (kæde, hooks, gates, jobs, nysgerrighed, DA, roller, fejlmønstre).
- Forslag om ubesøgte begreber, Docker-historien, genbrug fra GenAI Academy og et udkast til PR-plan.
- CertQuest-forsøgets forhåndsregistrering (PREREG, PROTOCOL, HANDOFF-CODEX).
- Harness engineering-sammenligningen (Claude Code, Codex, Pi, DeepSeek) og lektioner til V3.
