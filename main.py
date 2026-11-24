#!/usr/bin/env python3
"""One Word for Your Wi-Fi: writes a single word describing home Wi-Fi.

The word is "Ghosting": home Wi-Fi vanishes mid-call, mid-game, mid-download,
exactly like someone ghosting you -- there one second, gone the next, back
again with no explanation and no apology. Funny at once, true to how Wi-Fi
actually behaves, and a fresher angle than the usual "buffering" or "laggy".
The entry is written with no trailing newline so the file holds exactly the
word itself, 8 bytes.
"""

import os

WORD = "Ghosting"


def main() -> None:
    word = WORD.strip()
    assert 1 <= len(word) <= 20, "entry must be 1-20 characters"
    assert word.isalpha(), "entry must be a single word"
    assert not any(ch.isspace() for ch in word), "entry must have no spaces"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)
    print(f"wrote {len(word)}-byte entry to /output/entry.txt")


if __name__ == "__main__":
    main()
