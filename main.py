from pathlib import Path
import shutil

PLAYLIST_DIR = Path(__name__).parent / 'playlists'
MUSIC_DIR = Path('/music')

# Quick script to copy files from playlists into /import/Playlists/<file directory>, preserving directory structure
# For later addition to Navidrome


for playlist in PLAYLIST_DIR.iterdir():
    count = 0
    with playlist.open(encoding='utf8') as f:
        for l in f.read().splitlines():
            path = Path(l)
            if 'music' in path.parts:
                newpath = Path(*path.parts[:1], 'import', *path.parts[2:])
                if newpath.exists():
                    dir = Path('/import') / 'Playlists' / playlist.stem
                    dir.mkdir(exist_ok=True)
                    (dir / (Path(*newpath.parts[2:])).parent).mkdir(exist_ok=True)
                    shutil.copy(newpath, dir / Path(*newpath.parts[2:]))
                    count += 1
        print(count)