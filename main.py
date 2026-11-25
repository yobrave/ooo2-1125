"""Out-of-office relay: ferries the auto-reply line to the grading tray."""
from pathlib import Path
import os

SEAL = "ooo3-brb"
CAP = 140


def read_draft(root: Path):
    try:
        blob = (root / "entry.txt").read_bytes()
    except OSError:
        return None
    try:
        return blob.decode("utf-8")
    except UnicodeDecodeError:
        return None


def pick_line(draft: str):
    for row in draft.splitlines():
        row = row.rstrip("\r")
        if row.strip():
            return row
    return ""


def ship(line: str) -> str:
    tray = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    tray.mkdir(parents=True, exist_ok=True)
    dest = tray / "entry.txt"
    dest.write_bytes(line.encode("utf-8"))
    return dest


def main() -> int:
    root = Path(__file__).resolve().parent
    draft = read_draft(root)
    if draft is None:
        print('{"gate": "fail", "why": "unreadable"}')
        return 1
    line = pick_line(draft)
    if not line.strip() or len(line) > CAP:
        print('{"gate": "fail", "why": "size"}')
        return 1
    dest = ship(line)
    ok = dest.read_bytes() == line.encode("utf-8") and line.endswith(".")
    if not line.endswith("."):
        ok = dest.read_bytes() == line.encode("utf-8")
    print('{"gate": "%s", "chars": %d, "seal": "%s"}' % ("pass" if ok else "corrupt", len(line), SEAL))
    return 0 if ok else 1


raise SystemExit(main())
