from pathlib import Path
import shutil

PLAYLIST_DIR = Path(__file__).parent / 'playlists'
MUSIC_DIR = Path('/import') # Path of directory to import music from

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
                    dir = MUSIC_DIR / 'Playlists' / playlist.stem
                    dir.mkdir(exist_ok=True, parents=True)
                    (dir / (Path(*newpath.parts[2:])).parent).mkdir(exist_ok=True, parents=True)
                    shutil.move(newpath, dir / Path(*newpath.parts[2:]))
                    count += 1
        print(f'{playlist.stem}: {count}')