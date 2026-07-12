# decision-log-linker

A dependency-free CLI for linking ADR records to source, PR, and deployment evidence.

## Quick start

```bash
python linker.py adrs.json references.json
```

ADRs have IDs and optional `superseded_by`; references point back with an `adr` field. The report builds reverse links and classifies each decision as linked, unimplemented, or superseded.

## Test

```bash
python -m unittest discover -v
```

## License

MIT.
