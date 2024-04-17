# Beet

To run, do `docker compose run beet <command>`.

## Importing Music Files

- Place files in `/mnt/storage/Music - Import`
- Run `beet import /import` (aliased to the above `docker` command)
- If you want to tag them to a playlist, add an appropriate tag to the `comments` field (via `beet modify <query> comments=<value>`) after importing
- Note: Navidrome will not detect `.mp4` containers

## Importing an existing library with playlists

The best way (after trying multiple methods) is:

- Make a copy of the whole library
- Move files in playlists to their named folders (unfortunately, this won't work with files which are in multiple playlists)
- Do `beet import -A --set=comments=<playlistname> <playlistdir>` for each playlist directory. This tags the files (in the `comment` field) with the playlist they are in, so they can be queried later.
- Import the rest of the library with `beet import -A <musiclibrary>`.

## Updating

`pdm update -u`