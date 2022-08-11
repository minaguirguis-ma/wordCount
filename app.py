#Initial Commit
import lyricsgenius
import nltk
import collections
from collections import Counter

genius = lyricsgenius.Genius("-5FNOZho_II0RPhtTdHiP9hXpKXrLBXx-20NCQaenJq_FXqggK8mQy6tayKFD9Ru")

artist = genius.search_artist("Steve Lacy", max_songs=1, sort="title")
song = artist.song("Bad Habit")
songL = song.lyrics
print(songL)
