#!/usr/bin/env python3
"""Out of Tokens Mid-Sentence — one-line entry generator.

Writes the entry text to the output directory after validating it against
the competition gate: exactly one line, 1-140 characters, valid UTF-8, no
control characters, no leading/trailing whitespace.
"""

import hashlib
import os
import sys
import unicodedata

ENTRY = (
    "The apology cut off mid-sentence: 'Dear customer, "
    "your refund is approved, and\u2014' "
    "Support pasted 'and\u2014' into ticket #4821 three days ago."
)

MAX_CHARS = 140


def validate(text: str) -> None:
    """Raise ValueError if the entry breaks any gate rule."""
    if not text:
        raise ValueError("entry is blank")
    # UTF-8 round-trip: encoding the text and decoding it back must give
    # exactly the same string, so no character is silently replaced or
    # dropped by an encoding step between here and the grader.
    if text.encode("utf-8").decode("utf-8") != text:
        raise ValueError("entry does not survive a UTF-8 round-trip")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    for ch in text:
        if ord(ch) < 0x20 and ch not in ("\t",):
            raise ValueError(f"entry contains control character U+{ord(ch):04X}")
    # Reject invisible Unicode format characters (category Cf: zero-width
    # space, word joiner, etc.) and non-breaking spaces: they would change
    # the entry's byte count and gate result without changing what a reader
    # sees, so an invisible prefix could silently alter the entry.
    for ch in text:
        if unicodedata.category(ch) == "Cf" or ch == "\u00a0":
            raise ValueError(f"entry contains invisible character U+{ord(ch):04X}")


def main() -> int:
    validate(ENTRY)
    data = ENTRY.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    # Read-back verification: the file on disk must be byte-identical to the
    # validated entry — no BOM, no trailing newline, no encoding drift.
    with open(out_path, "rb") as f:
        on_disk = f.read()
    if on_disk.startswith(b"\xef\xbb\xbf"):
        raise ValueError("output starts with a UTF-8 BOM")
    if on_disk != data:
        raise ValueError("read-back mismatch: file on disk differs from entry")
    digest = hashlib.sha256(on_disk).hexdigest()
    print(f"chars: {len(ENTRY)}")
    print(f"bytes: {len(data)}")
    print(f"sha256: {digest}")
    print(f"wrote: {out_path} (read-back verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
