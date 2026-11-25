"""Out-of-office one-liner: gate + export, run 4."""
import json
import os
import pathlib

RANGE = (1, 140)
CODEWORD = "ooo4-out-of-office-r4"


def collect():
    return (pathlib.Path(__file__).resolve().parent / "entry.txt").read_text(encoding="utf-8").strip()


def within(n):
    lo, hi = RANGE
    return lo <= n <= hi


def commit(text):
    d = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    d.mkdir(parents=True, exist_ok=True)
    (d / "entry.txt").write_bytes((text + "\n").encode("utf-8"))


body = collect()
n = len(body)
ok = within(n)
if ok:
    commit(body)
print(json.dumps({"codeword": CODEWORD, "chars": n, "within": ok, "range": RANGE, "run": 4}))
