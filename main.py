"""The Self-Checkout Is Judging You.

Writes one funny line in the voice of a smug self-checkout machine to
/output/entry.txt (or the path the environment asks for).

Stdlib only. Deterministic bytes on every run.
"""

import os

LINE = "You scanned the wine before the baby food. Priorities noted. Judgment logged. Have a day."


def resolve_output_path():
    explicit = os.environ.get("ENTRY_OUTPUT")
    if explicit:
        return explicit
    for key in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(key)
        if directory:
            return os.path.join(directory, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main():
    text = LINE
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("entry must not be whitespace only")
    path = resolve_output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
