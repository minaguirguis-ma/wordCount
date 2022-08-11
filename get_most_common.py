import lyricsgenius
from collections import Counter
import string
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist
import plotly.express as px
import pandas as pd

genius = lyricsgenius.Genius("-5FNOZho_II0RPhtTdHiP9hXpKXrLBXx-20NCQaenJq_FXqggK8mQy6tayKFD9Ru")

artist = genius.search_artist("Steve Lacy", max_songs=1, sort="title")

song = artist.song("Bad Habit")
songL = song.lyrics
print(songL)

stop_words = set(stopwords.words('english'))
f = open('BadHabit.txt')
lines = f.readlines()
all_tokens = []
for line in lines:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    word_tokens = word_tokenize(line)
    filtered = [w for w in word_tokens if not w.lower() in stop_words]
    all_tokens = all_tokens + filtered
fdist = FreqDist(all_tokens)
print(fdist.most_common(10))


dataDisplay = [(fdist.most_common(10)[0][0], fdist.most_common(10)[0][1]), 

(fdist.most_common(10)[1][0], fdist.most_common(10)[1][1]),
(fdist.most_common(10)[2][0], fdist.most_common(10)[2][1]),
(fdist.most_common(10)[5][0], fdist.most_common(10)[5][1]),
(fdist.most_common(10)[6][0], fdist.most_common(10)[6][1]),

]
df = pd.DataFrame(dataDisplay, columns=["words", '# of occurences'])
# print(df)
fig = px.bar(df, x='words', y='# of occurences')
fig.show()



