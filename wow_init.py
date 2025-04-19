import os
from pathlib import Path

folders = [
    ".patches", ".metrics", "logs", "docs", "scripts", "docs/handoff", "docs/history"
]
logs = ["logs/changelog.yaml", "logs/thought_trace.yaml", "logs/handoff_log.yaml"]

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

for log in logs:
    path = Path(log)
    if not path.exists():
        path.write_text("[]\n")

print("[OK] AI Delivery Kit initialized.")
