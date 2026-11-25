"""Out-of-office one-liner: gate + export, run 4."""
import json
import pathlib

RANGE = (1, 140)
CODEWORD = "ooo4-out-of-office-r4"


def collect():
    return pathlib.Path("entry.txt").read_text(encoding="utf-8").strip()


def within(n):
    lo, hi = RANGE
    return lo <= n <= hi


def commit(text):
    d = pathlib.Path("out")
    d.mkdir(exist_ok=True)
    (d / "entry.txt").write_bytes((text + "\n").encode("utf-8"))


body = collect()
n = len(body)
ok = within(n)
if ok:
    commit(body)
print(json.dumps({"codeword": CODEWORD, "chars": n, "within": ok, "range": RANGE, "run": 4}))
