# ADR-0001: Kontrakter versioneres via PR

- **Status:** Accepted (operatøren, 2026-10-20; B-014)
- **Dato:** 2026-10-20
- **Erstatter:** —

## Kontekst

V2 har 115 forskellige `anchor.*.vN`-skemaer spredt over koden og intet sted, der samler dem
(målt 2026-10-20). Atlasset i V2 krævede meget arbejde at holde opdateret, fordi læring, levende tal og
definitioner stod på de samme sider.

## Beslutning

1. En kontrakt er én fil, `contracts/<id>.json`, med `version` (MAJOR.MINOR), `status`, `changelog`,
   oprindelse og links til ADR'er, kode og tests.
2. En kontrakt ændres kun via PR. Ændres dens indhold, skal versionen hæves (fx `scdd` 0.1 → 0.2), og
   der skal være en changelog-linje for den nye version.
3. En kontrakt slettes aldrig. Den får status `Superseded`, så alt, der citerer `id@version`, kan spores.
4. CI håndhæver reglen: `tools/check_contracts.py --base <base-gren>` fejler PR'en ved brud.
5. Anchor Atlas genereres fra kontrakter og ADR'er ved merge; ingen vedligeholder det i hånden.

## Konsekvenser

- En beslutning på kæden kan sige, hvilken regel den blev taget under (`besluttet under scdd@0.1`).
- At ændre en regel bliver synligt og reviewbart; en tavs ændring kan ikke merges.
- Prisen er en lille ceremoni pr. ændring (version + changelog). Den er bevidst lille.
