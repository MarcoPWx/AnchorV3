# Data: hvad vi har, hvor det skal bo, og hvad det skal bruges til

Anchor er større i data, end man tror. Alle tal er målt 2026-10-20 i V2 (`vocali` @ `054a6989c`) og er
OBSERVED, selvmålt.

| Hvad | Mængde | Kommando |
|---|---|---|
| Commits i V2-repoet | 2.510 (1.629 rører `packages/anchor`, 782 rører `.anchor`) | `git rev-list --count HEAD [-- sti]` |
| Kæden | 379.000 events, 78 event-typer, 269 MB; 12 typer har under 10 events | stream `chain.jsonl`, tæl `event_type` |
| Største event-typer | model_call 45.990 · awareness_probe 45.543 · verification 42.422 · humean_check 38.788 · pile_sedimented 34.372 · suggestion_emitted 32.458 · suggestion_disposed 32.434 · classification_detected 20.363 | samme |
| DuckDB (`atlas.duckdb`) | 4,8 GB; hele `.anchor/runtime` 6,7 GB | `ls -lh`, `du -sh` |
| Filer under git | 33 TSV, 606 JSONL; `corbell-data/` 195 MB | `git ls-files`, `du -sh` |

## Hvor data skal bo i V3 (B-007)

| Lag | Rolle | Sandhed? |
|---|---|---|
| **Kæden** (append-only, én pr. projekt) | Hvad der skete, i rækkefølge, med kvitteringer | **Ja**, for hændelser |
| **Git** (kode, registret som JSON, draws) | Hvad der er besluttet og bygget; review via PR | **Ja**, for indhold |
| **DuckDB** | Afledt analyse-lager: ledger, dækning, videnskab, benchmarks. Bygges af én producent på kadence og kan altid genbygges | **Nej**, aldrig kilde |
| **Registret** | Projektets kort: begreber, fakta med dato og kilde, links | Ja, i git |

Ikke én monolit på 4,8 GB: separate, genbyggelige filer pr. formål, med en note om, hvad der kan slettes.

## Embeddings og RAG: ikke i første skive

Anchors løfte er, at de **krævede** kilder og tidligere rettelser når agenten. Det afgøres af autoritet,
anvendelighed og **eksplicitte relationer** (draws, ADR'er, beslutninger, registerlinks), ikke af lighed.
Roadmappens regel: *relevans foreslår, autoritet afgør* (bid 8), og en påkrævet rettelse skal nå frem, selv om
den ikke deler ord med opgaven (bid 17).

- **V3 starter med** leksikalsk søgning + eksplicitte links.
- **Embeddings kommer ind som forslagsgiver** (bid 13, med målt præcision), først når en måling viser, at
  leksikalsk søgning + links misser krævede kilder.
- **Advarsel fra V2:** 214.862 L4-chunks med vektorer, men 0 rækker i doc↔kode-provenance (målt 2026-10-20,
  RELAYED). Vektorer uden provenance kan ikke sige, hvorfor noget blev fundet.

## Flowet

repo + kæde + TSV → producent (på kadence) → DuckDB (afledt) → fakta med dato og kilde i registret →
TUI, Atlas og MCP. Agentens kontekst er en afgrænset lukning over eksplicitte relationer, leveret via MCP.

## Forskning: Zenodo, benchmark og senere Databricks

- **Datasæt til Zenodo:** et data-inventar (PR 2) + et datasheet pr. datasæt (hvad, hvordan indsamlet, hvad det
  ikke kan bruges til) + forhåndsregistreringer. Negative resultater publiceres også.
- **Benchmark:** CertQuest-forsøget (B-012) er første gang, Anchor måles mod en vært uden Anchor.
- **Databricks senere:** eksport til Parquet som udvekslingsformat. Lokal-først indtil en konkret analyse kræver
  mere. **Før enhver eksport:** fjern hemmeligheder og persondata, og mærk hvert datasæt med kilde og version.
