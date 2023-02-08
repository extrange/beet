# Beet

To run, do `docker compose run beet <command>`.

# Importing an existing library with playlists

The best way (after trying multiple methods) is:

- Make a copy of the whole library
- Move files in playlists to their named folders (unfortunately, this won't work with files which are in multiple playlists)
- Do `beet import -A --set=comments=<playlistname> <playlistdir>` for each playlist directory. This tags the files (in the `comment` field) with the playlist they are in, so they can be queried later.
- Import the rest of the library with `beet import -A <musiclibrary>`.