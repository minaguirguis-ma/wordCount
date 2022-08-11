import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist

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