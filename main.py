from pathlib import Path

ENTRY = "fix: auto-merged my own PR at 3:12am, CI was red; prod is redder, intern is explaining it to the CEO and I marked the incident resolved"

Path("/output/entry.txt").write_text(ENTRY, encoding="utf-8")
