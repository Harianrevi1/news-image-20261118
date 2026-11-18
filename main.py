"""Entry program for make.fun bounty news-image-20261118.

The news image for Wednesday 18 November 2026 lives in this repository
as entry.png. This program copies it, byte for byte, to the output
directory the grader provides, as /output/entry.png.

Standard library only, no network, fully deterministic: every run
writes exactly the same bytes.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"bundled image missing: {source}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    destination = out_dir / "entry.png"
    shutil.copyfile(source, destination)
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
