# Beet

To run, do `docker compose run beet <command>`.

## Importing Music Files

- Place files in `/mnt/storage/Music - Import`
- Run `beet import /import` (aliased to the above `docker` command)
- If you want to tag them to a playlist, add an appropriate tag to the `comments` field (via `beet modify <query> comments=<value>`) after importing
- If a field is unknown, when editing, remove it instead of giving the empty string `''`. This prevents Navidrome from listing it
- Use the GUI tag editor `kid3` to mark tracks as toprated (in the `comments` field)

Note: Navidrome will not detect `.mp4` containers

## Modifying metadata for specific paths in the library

`beet mod /path/to/album field='value'`

## Move files to correct locations

`beet update` and `beet move` don't seem to move files in the library. I manually move them out, do `beet update` (which deletes them from the database), then reimport them again.

Beet has the following catch-all folders:

- `compilations`: check that songs/albums don't get sent here accidentally
- `_`: unknown albums
- `Non-Album`: singleton tracks
- `Various Artists`

## Check files in library which are not in database

## Import Rules

- No/unknown artist/album: set as `''` (**not just blank**, that will create a folder with the name `None`)
- Always import songs as albums, if available, even if incomplete (i.e. never as singletons/`T`)
- Sometimes songs seemingly not part of any album might be singles (e.g. MaxKoMusic)

## Importing an existing library with playlists

The best way (after trying multiple methods) is:

- Make a copy of the whole library
- Move files in playlists to their named folders (unfortunately, this won't work with files which are in multiple playlists)
- Do `beet import -A --set=comments=<playlistname> <playlistdir>` for each playlist directory. This tags the files (in the `comment` field) with the playlist they are in, so they can be queried later.
- Import the rest of the library with `beet import -A <musiclibrary>`.

## Adding titles/subtitles to discs

For albums with many discs, you can add the name of the disc by adding a `TSST` field to all tracks in the same disc.

## Updating this repo

`pdm update -u`