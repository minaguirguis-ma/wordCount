#Initial Commit
import lyricsgenius

genius = lyricsgenius.Genius("-5FNOZho_II0RPhtTdHiP9hXpKXrLBXx-20NCQaenJq_FXqggK8mQy6tayKFD9Ru")

artist = genius.search_artist("Steve Lacy", max_songs=1, sort="title")

print(artist.songs)