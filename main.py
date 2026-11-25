"""Write one unsent micro-confession to entry.txt.

Reads MAKEFUN_OUTPUT_DIR (default /output), creates it, and writes
exactly one line plus a trailing newline. Standard library only.
"""

import os
from pathlib import Path

CONFESSION = (
    "I still water the plant you left behind, and I talk to it sometimes, "
    "because it's the only thing in this flat that never left me on read."
)


def main() -> None:
    line = CONFESSION
    if not line:
        raise ValueError("confession must not be empty")
    if len(line) > 170:
        raise ValueError("confession must be at most 170 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("confession must be a single line")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
