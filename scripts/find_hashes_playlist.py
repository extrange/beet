# Find hashes for files in a playlist, and saves to a csv file

import csv
from pathlib import Path

# Directory storing playlists (with one path per line)
PLAYLISTS_TXT_DIR = Path(__file__).parent.parent / "playlists_txt"

# csv file containing all hashes of audio files in /mnt/storage/Music
HASHES_FILE = Path(__file__).parent.parent / "hashes.csv"

# Output directory of playlist files with their hashes
OUTPUT_DIR = Path(__file__).parent.parent / "playlists_hashes"

hashes = {}

with open(HASHES_FILE, newline="") as f:
    reader = csv.reader(f)
    hashes = {k: v for k, v in reader}


for txt in PLAYLISTS_TXT_DIR.glob("*.m3u"):
    playlist_hashes = []
    with open(txt) as f:
        # Load filepaths
        for line in f.read().splitlines():
            # Lookup hashes
            hash = hashes[line]
            playlist_hashes.append([line, hash])
    with open(OUTPUT_DIR / f"{txt.stem}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(playlist_hashes)
