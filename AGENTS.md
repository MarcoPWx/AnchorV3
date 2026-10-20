# AGENTS.md — læs dette først

Kort pegepind, ikke en manual. Detaljer står i de filer, der linkes til.

## Regler

1. **Én PR = ét begreb eller én bid** ([docs/PLAN.md](docs/PLAN.md)). Hold PR'en lille nok til, at operatøren
   forstår hver fil.
2. **Test først.** Skriv den fejlende test, se den fejle af den rigtige grund, skriv så den mindste kode.
3. **Oprindelse.** Kode eller data fra V2 angives som `V2-sti @ sha` i PR-beskrivelsen. Intet kopieres i bulk.
4. **Rør aldrig V2's runtime.** Skriv aldrig i `vocali/.anchor/runtime/`. Sæt aldrig `ANCHOR_CHAIN_PATH`.
   Kør aldrig V2's `anchor`-kommandoer inde i fixtures: de skriver på den levende kæde.
5. **Ét hjem pr. slags viden** ([README.md](README.md)): status i Linear, design-hensigt i Sketch, hændelser
   i kæden, kode og register i git. Skriv aldrig samme status to steder.
6. **Tal har dato, kilde og trin** (OBSERVED / RELAYED / CLAIMED). Selvmålte resultater loftes ved OBSERVED.
7. **Beslutninger tages af operatøren.** En agent foreslår; spørgsmål, der kræver valg, stilles i PR'en.

## Hvor ting bor

| Hvad | Sti |
|---|---|
| Beslutninger | [docs/BESLUTNINGER.md](docs/BESLUTNINGER.md) |
| Plan og første PR'er | [docs/PLAN.md](docs/PLAN.md) |
| Data, lagring, RAG, forskning | [docs/DATA.md](docs/DATA.md) |
