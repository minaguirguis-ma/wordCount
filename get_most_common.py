import string
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist
import plotly.express as px
import pandas as pd

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

dataDisplay = (fdist.most_common(10)[0])
df = pd.DataFrame(dataDisplay, columns=['x', '# of occurences'])

fig = px.bar(df, x='words', y='# of occurences')
