# Check if all the files in a list exist

from pathlib import Path

with open('playlists_txt/chanel.m3u') as f:
    for line in f.readlines():
        p = Path(line.strip())
        if not p.exists():
            print(p)