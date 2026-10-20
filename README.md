# Anchor V3

**Når du arbejder med en AI-agent i dit repo, sørger Anchor for, at agenten får det rigtige at vide, at du
kan se, hvad den gjorde, og om det holder, og at arbejdet kan fortsætte i morgen. Undervejs lærer Anchor
dig dit eget projekt.**

V3 starter tomt med vilje. Alt fra V2 (`vocali/packages/anchor`) kommer kun ind gennem en PR, der
begrunder genbruget med evidens og angiver sin oprindelse (`V2-sti @ sha`). Så forstår vi hver fil, når
den lander.

## Hvad er hvad

| Del | Hvad det er | Hvor |
|---|---|---|
| **Anchor** | Produktet. **TUI-først**: arbejdsfladen ved siden af agenten. Projektets kort, opgaven her og nu, HIL med én tast | dette repo |
| **Anchor Atlas** | Produktmanual og læring. HTML genereret fra samme register; åbnes med `?` eller `b` fra TUI'en | dette repo (`atlas/`) |
| **Linear** | Opgaver og deres status, roadmappen (team ANC3) | linear.app |
| **Sketch** | Tegnebræt for design-hensigt: arkitektur og diagrammer til draws. Aldrig status eller tal uden dato | Sketch-dokumentet "Anchor" |
| **Git** | Kode, registret og draws som tekst; review via PR | dette repo |
| **Kæden** | Hvad der faktisk skete. Beviser UÆNDRET, aldrig SAND | runtime pr. projekt |

## Sådan arbejder vi

- **Én PR = ét begreb eller én bid** fra roadmappen, med tests skrevet først og en opdateret atlas-række.
- Operatøren reviewer hver PR. Intet merges uden review.
- Beslutninger står i [docs/BESLUTNINGER.md](docs/BESLUTNINGER.md), planen i [docs/PLAN.md](docs/PLAN.md),
  og datagrundlaget i [docs/DATA.md](docs/DATA.md). Agenter læser først [AGENTS.md](AGENTS.md).

## Status (2026-10-20)

Kun grundlaget. Ingen kode endnu. Roadmappens kanoniske hjem er Linear-dokumentet
[V3-roadmap, flettet 20. okt.](https://linear.app/anchored/document/v3-roadmap-flettet-20-okt-laesemaskinen-bid-for-bid-20-bidder-0daff2acfe61).
