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

- beet says there are ____