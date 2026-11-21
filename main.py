"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (UTF-8, one line, 1-280 chars).
Deterministic, stdlib only, no network.
"""

import os

JOKE = (
    "My AI coding agent reviewed my pull request, fixed the bug, "
    "and approved it \u2014 then asked me to review its review, "
    "because apparently I'm still in the loop for emotional support."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"joke is {len(text)} chars"
    assert "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
