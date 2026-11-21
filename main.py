"""Entry for make.fun "The poem about permission".

Writes a short original poem about agency -- the power to ask and to
be given -- to $MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic: the same
poem, byte for byte, on every run.

The poem is 232 Unicode code points (236 bytes UTF-8), inside the
gate's 1-280 character limit.
"""

import os

POEM = (
    '"Ask," I said, and the door\n'
    "did not open.\n"
    "It waited, the way doors do,\n"
    "for a hand that was not mine.\n"
    "\n"
    "So I asked again, softer \u2014\n"
    "not for the door, but for the key \u2014\n"
    "and someone on the other side\n"
    "turned it, and called the room mine.\n"
)


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
