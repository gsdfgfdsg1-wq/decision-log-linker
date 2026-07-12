#!/usr/bin/env python3
"""Link architecture decisions to implementation and delivery evidence."""
import argparse
import json
from collections import defaultdict
from pathlib import Path


def link(adrs, references):
    by_id = {adr["id"]: adr for adr in adrs}
    evidence = defaultdict(list)
    for ref in references:
        if ref.get("adr") in by_id: evidence[ref["adr"]].append(ref)
    decisions = []
    for adr_id, adr in sorted(by_id.items()):
        refs = evidence[adr_id]
        state = "superseded" if adr.get("superseded_by") else "unimplemented" if not refs else "linked"
        decisions.append({"id": adr_id, "title": adr.get("title", ""), "state": state, "references": refs})
    return {"decisions": decisions, "unimplemented": [item["id"] for item in decisions if item["state"] == "unimplemented"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("adrs"); parser.add_argument("references")
    args = parser.parse_args()
    print(json.dumps(link(json.loads(Path(args.adrs).read_text()), json.loads(Path(args.references).read_text())), indent=2))


if __name__ == "__main__":
    main()
