"""Five Seconds to Explain the Glass.

Joke angle: cat vanity. The cat mistakes its own reflection in the
glass for a handsomer rival cat, so knocking the glass over is framed
as turf defence rather than an accident -- self-interest, no remorse.
"""

import os

ENTRY = "It kept reflecting a much handsomer cat, and I refuse to share this house with a rival that handsome."


def main() -> None:
    line = ENTRY
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        raise ValueError("entry must not contain control characters")
    data = line.encode("utf-8")
    if len(data) > 200:
        raise ValueError("entry must be at most 200 UTF-8 bytes")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
