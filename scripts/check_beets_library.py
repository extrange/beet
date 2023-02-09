# Compare all tracks' hashes to beet's hashes, and check those which are missing from beets' library
import csv

BEET_HASHES_TXT = "beet_hashes.txt"
TRACK_HASHES_CSV = "hashes.csv"

# Get all hashes currently in beets
beet_hashes = []
with open(BEET_HASHES_TXT) as f:
    for line in f.readlines():
        beet_hashes.append(line.strip())
count = 0
# Read current library's tracks and hashes
with open(TRACK_HASHES_CSV, newline="") as f:
    reader = csv.reader(f)
    for name, hash in reader:
        if hash not in beet_hashes:
            print(f"{name}: {hash}")
            count += 1

print(count)
