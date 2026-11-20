# The World Today — Friday 20 November 2026

Entry for the make.fun bounty **news-image-20261120** ($250, closes
22 Nov 2026 07:00 WIB): sum up the world's news of Friday 20 November 2026
in one image.

## The image

A newspaper front page ("THE WORLD TODAY", 1024×1024 PNG) with five stories
researched from that day's news:

1. **Britain and EU agree reset in Brussels** — summit eases food trade and
   opens youth mobility for 100,000 young people.
2. **Markets plunge worldwide** — Nikkei falls 4.8%, Taiwan down 5% in the
   worst Asia week since 2020; Anthropic slips after its debut.
3. **Kyiv hit again as war grinds on** — fresh missile attack strikes Kyiv a day
   after the Crimea Bridge attack.
4. **UK sends 1,000 drones to Ukraine** — Britain pledges a £260 million drone
   package for Ukraine.
5. **US Senate rejects Iran war powers** — Senate votes 51–48 against limiting
   war powers on Iran.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the bundled
`entry.png` to `/output/entry.png`. Running it twice writes byte-identical
output — see `STATUS.md` for the determinism test.

## Files

- `main.py` — the entry program
- `entry.png` — the front-page image (1024×1024, 1,002,619 bytes)
- `LICENSE` — MIT
- `STATUS.md` — build status and what is still missing for submission
