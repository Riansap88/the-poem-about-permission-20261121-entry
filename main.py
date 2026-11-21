import os
from pathlib import Path

POEM = """For years I polished my silence like a coin,
saving it for a day that never came.
Then I spent it on two small words —
may I? — and the world, surprised,
answered yes, as if the lock
had only ever been a door
left ajar by everyone
too polite to push."""

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(POEM, encoding="utf-8")
