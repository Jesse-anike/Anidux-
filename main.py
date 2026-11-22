from __future__ import annotations
import argparse
import collections
import json
import sys
from pathlib import Path


def analyze(text: str) -> dict:
    counts = collections.Counter()
    originals = {}
    invalid = 0
    for line in text.splitlines():
        if not line.strip():
            continue
        try:
            alert = json.loads(line)
        except json.JSONDecodeError:
            invalid += 1
            continue
        key = json.dumps(alert, sort_keys=True, separators=(",", ":"))
        counts[key] += 1
        originals[key] = alert
    return {
        "input_events": sum(counts.values()),
        "unique_count": len(counts),
        "invalid_lines": invalid,
        "unique_alerts": [
            {"occurrences": count, "alert": originals[key]}
            for key, count in counts.most_common()
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Deduplicate JSONL security alerts.")
    parser.add_argument("input", nargs="?", default="-", help="JSONL file; defaults to stdin")
    parser.add_argument("--output", help="Optional output JSON file")
    args = parser.parse_args()
    raw = sys.stdin.read() if args.input == "-" else Path(args.input).read_text(encoding="utf-8")
    result = analyze(raw)
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
