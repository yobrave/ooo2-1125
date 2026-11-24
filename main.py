"""Out-of-office line ferry.

Writes one line, walks it back once, and reports the round trip in a
tiny verdict. No arguments, no network, nothing else to declare.
"""
import os

LINE = ("Out of office until Monday. The inbox and I have agreed to "
        "see other people.")
V = "ooo2"
TRIP = 2


def ferry(base):
    base = base or "output"
    if not os.path.isdir(base):
        os.makedirs(base)
    p = os.path.join(base, "entry.txt")
    f = open(p, "w", encoding="utf-8", newline="\n")
    f.write(LINE)
    f.close()
    r = open(p, encoding="utf-8")
    t = r.read().strip()
    r.close()
    assert t == LINE, "ferry lost cargo"
    return t


t = ferry(os.environ.get("MAKEFUN_OUTPUT_DIR"))
print(V, "roundtrip", TRIP, len(t))
