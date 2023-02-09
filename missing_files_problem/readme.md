# Files

- `tracks.txt`: All music files (as per `ffprobe` check) in `/mnt/storage/Music` as of 8/2/23
- `hashes.csv`: `murmur3` hashes for all music files in `tracks.txt`

## `murmur3` hashing

- `c:a copy` must be set, otherwise re-encoding happens which changes the checksum across `ffmpeg` versions
- `-map 0:a` isolates only the audio portion, otherwise the hash includes embedded video/photo information (present in some files)

## Playlist counts

- Psychedelic: 2
- Top Rated: 578
    - navidrome has 579
    - ./Unknown/Mirror's Edge- Original Videogame Score/11 Mirror's Edge - Still Alive (The Theme From Mirror's Edge).flac is a duplicate
    - Mr Brown track is deleted
- chanel: 48

## Total Library Count

- Navidrome says there are 4576 songs total - probably not picking up all
- `ffprobe` says there are 4597

## Import prior to 9/2/23

- beet says there are 4596 songs
- after deleting 148 duplicates there were 4448

## Import 9/2/23

- beet says there are 4596 songs
    - This file was not imported: `/mnt/storage/Music/Various Artists/Initial D ~D Selection~/02 Edo Boys - No One Sleep In Tokyo.mp3:murmur3=f9277ba7e3df5dd20a28f0b05c73590b`
    - After importing this file, there were 4597 songs
- This file was not detected by ffprobe (why?): `/mnt/storage/Music/Unknown/R Type/00 Midis - R-TYPE - ENDING`NAME - Piano Ver..mp3`
    - However, it was detected by `beets` and imported
- This file was (likely) not imported by `beets`: `/mnt/storage/Music/Telegram/.trashed-1674299154-AUD-20221222-WA0017.opus,murmur3=a950deee6d29858305b4537b80eac931`

- Playlists:
    - Before deleting duplicates:
        - `toprated`: 602
        - `chanel`: 48
        - `psychedelic`: 2
        - Probably the reason why `toprated` has some extras is because there are some duplicates there
    - After deleting 145 duplicates there were 4452 songs
        - `toprated`: 578

- Navidrome says there are 4431 songs...
    - Playlist counts however, are correct