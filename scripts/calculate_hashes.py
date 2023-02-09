# Calculate hashes for all files in current library (given by 'tracks.txt')
# This file must be run from the host (not from the container)

from pathlib import Path
import subprocess
import csv
import shlex

hashes = []

with open("tracks.txt") as f:
    for line in f.readlines():
        p = Path(line.strip())
        # Can't use shlex.split because some filenames have quotes
        proc = subprocess.run(
            [
                "/usr/bin/ffmpeg",
                "-hide_banner",
                "-loglevel",
                "error",
                "-i",
                p,
                "-map",
                "0:a",
                "-c:a",
                "copy",
                "-f",
                "hash",
                "-hash",
                "murmur3",
                "-",
            ],
            capture_output=True,
            text=True,
        )
        hash = proc.stdout.strip()
        print(f"{p}: {hash}")
        hashes.append({"file": p, "hash": hash})

with open("hashes.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["file", "hash"])
    writer.writerows(hashes)
