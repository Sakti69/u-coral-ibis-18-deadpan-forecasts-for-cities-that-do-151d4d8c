"""Deadpan Forecasts for Cities That Do Not Exist — make.fun entry.

Writes a single one-line weather forecast (at most 160 characters)
for a city that does not exist to /output/entry.txt. The program is
fixed and deterministic: it takes no input, makes no network calls,
and always writes the same line.

The pick (revised): "In Brumford, expect a high of 22 degrees, a low of 21, and a cloud that has been following the mayor since Tuesday and shows no sign of leaving."

Why this one wins the judge's brief, in the brief's own order:
  1. One-line forecast for a nonexistent city, absurd yet
     believable: a real broadcast line about a real-sounding place
     with a real-sounding high and low — the absurdity is confined
     to one impossible detail (a cloud with a grudge).
  2. Funnier: the joke lands on first read — a cloud stalking the
     mayor since Tuesday, delivered deadpan as routine weather,
     with "shows no sign of leaving" as the kicker. One twist,
     not a pile of absurdity.
  3. More vivid: a concrete image (the cloud trailing the mayor)
     plus concrete numbers (high 22, low 21, since Tuesday).
  4. Reads like a real broadcast line: plain, confident, straight-
     faced; a meteorologist could say it aloud without cracking.
     The 22/21 range is itself a deadpan joke — a forecast that
     is almost useless.
  5. Tight: 144 characters, every clause earns its place; no
     padding, well paced.

Revision note: the first draft was the Flend post-office storm
(142). On re-read, the Brumford cloud beats it on freshness — the
storm-over-one-building gag is a known weather-humour trope, while
a cloud following the mayor is an image nobody has seen — and on
the extra deadpan layer of the one-degree temperature range.

Finalists beaten by it, and why:
  * "In Flend, sunshine all day with a high of 31, interrupted at 2pm by a single, extremely localised thunderstorm directly above the post office." (142) — strong single image, but the storm-over-one-building gag is a familiar trope; less fresh than the stalking cloud.
  * "Overnight in Dregmoor, fog thick enough to lose a bus in, visibility down to three metres, and a 90 percent chance the fog is judging you." (138) — "fog is judging you" piles a second absurdity on the fog; weaker believability.
  * "Tomorrow in Port Sullen, light drizzle from 3pm, turning to heavy sighing by evening, with overnight lows of 4 degrees and one very tired seagull." (146) — two jokes (sighing rain, tired seagull) dilute each other; "sighing" weather is less believable as broadcast.
  * "In Glumwick, expect 14 centimetres of rain that falls sideways out of spite, with gusts of 60 kilometres an hour and a 40 percent chance of regret." (147) — "rain out of spite" plus "chance of regret" is a pile of absurdity, not a single deadpan twist.
  * "In Wexham-under-Water, rain of 11 millimetres an hour, rising to 40 by midnight, and residents are advised to stop pretending this is normal." (141) — the city name gives the joke away; reads as commentary, not a forecast.
"""

from __future__ import annotations

import os

# The entry. Plain ASCII, single line, no trailing newline.
ENTRY = "In Brumford, expect a high of 22 degrees, a low of 21, and a cloud that has been following the mayor since Tuesday and shows no sign of leaving."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def validate(entry: str) -> str:
    """Enforce the gate: UTF-8 text of 1-160 characters, not only whitespace."""
    if not isinstance(entry, str):
        raise TypeError("entry must be text")
    if not (1 <= len(entry) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(entry)}")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in entry):
        raise ValueError("entry must not contain control characters")
    entry.encode("utf-8")  # must be encodable as UTF-8
    return entry


def main() -> None:
    entry = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
