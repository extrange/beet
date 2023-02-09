# Call beets to tag files matcheng hashes in a csv file [filename, murmur3_hash]
# Used to tag files in a playlist within beets
# Uses filename as tag value, separated by spaces (e.g. 'toprated psychedelic')
# Similarity is determined by murmur3 hashes

# Run this script in docker container, as `beet` command might not be available

from pathlib import Path
import csv
import subprocess

PLAYLIST_HASH_DIR = Path(__file__).parent.parent / "playlists_hashes"

# Dict of {playlistname: list of (filepath, hash)}
hashes = {}

# Load filenames and hashes
for playlist in PLAYLIST_HASH_DIR.glob("*.csv"):
    with open(playlist, newline="") as f:
        reader = csv.reader(f)
        hashes[playlist.stem] = [(filename, hash) for filename, hash in reader]

    # For each file, in each playlist:
    # Load 'comments' field for item in beets library, using hash
    # Check if playlist name has been added, if not, append
    modified = 0
    for filename, hash in hashes[playlist.stem]:
        # Find and load comments field in beets
        comments = subprocess.run(
            f"beet ls -f '$comments' checksum:{hash}",
            shell=True,
            text=True,
            capture_output=True,
        ).stdout.strip()

        # If playlist not in the field, append and attempt write
        if playlist.stem not in comments.split():
            print(
                f"Playlist '{playlist.stem}' not found in {filename} (got '{comments}'), attempting add"
            )
            proc = subprocess.run(
                f"beet modify -y checksum:{hash} 'comments={(comments + ' ' + playlist.stem).strip()}'",
                shell=True,
                text=True,
                stderr=subprocess.STDOUT,
                stdout=subprocess.PIPE,
            )
            modified += 1

            # If there was an error, halt
            if proc.returncode != 0:
                raise RuntimeError(
                    f"Error while attempting to add playlist for {filename}:{hash}: {proc.stdout}"
                )
    # Print statistics
    print(
        f"Playlist '{playlist.stem}': Parsed {len(hashes[playlist.stem])} files, modified {modified}"
    )
