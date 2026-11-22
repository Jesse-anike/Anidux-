# Alert Deduplicator

Deduplicate JSONL alert exports using stable canonical JSON and retain occurrence counts.

## What it does

This is a defensive, read-only portfolio project. It produces structured findings for a human analyst; it does not exploit systems, change security settings, or take automated blocking actions.

## Requirements

- Python 3.10+
- Python standard library only (no third-party packages)

## Quick start

```bash
python --version
python main.py alerts.jsonl
```

For projects that take a directory, run against a directory you own or are authorized to assess. For log/data projects, provide an exported sample in the expected format. The included `sample.log` is synthetic and uses documentation-only IP addresses.

## Input and output

- Input: local files/directories or a single explicitly supplied endpoint where the README command indicates an HTTPS URL.
- Output: JSON to standard output. Some projects accept `--output FILE` to save the report.
- No credentials, API keys, or secrets are required.

## Validation

```bash
python -m unittest discover -s tests -v
python main.py --help
```

## Security and ethical use

Use only on systems, logs, cloud exports, and networks you own or have explicit permission to assess. Review every finding before taking action. This project is a learning/portfolio implementation, not a certified security product or a substitute for a full audit.

## Portfolio context

Built as part of Anike-Moses Melie Jesse's defensive cybersecurity and cloud-security engineering portfolio, emphasizing Python, Linux, log analysis, network defence, application security, and AWS security fundamentals. It is a self-directed portfolio project; do not describe it as a production deployment unless you independently deploy and validate it.
