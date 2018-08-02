# from stop_words import get_stop_words
# from nltk.corpus import stopwords
from nltk import sent_tokenize, word_tokenize, re
import codecs
import string

# stop_words = list(get_stop_words('en'))
# nltk_words = list(stopwords.words('english'))
# stop_words.extend(nltk_words)

# final_stop_words = list(set(stop_words))
# final_stop_words.extend([",", ".", "(", ")"])

file = open('document1.txt', 'r')

with open('document1.txt', 'rb') as f:
    text = f.read()

text = text.decode('utf-8', errors='ignore')
text = str(text)

sentences = sent_tokenize(text)
words = word_tokenize(text.translate(string.punctuation))

# words = [w.lower() for w in words]

words = [w for w in words if (not len(w) <= 2)]

# words = [w.replace(",", "") for w in words]

# u.s.a drops
words = [w for w in words if w.isalpha()]
with open(file="1.txt", mode="w+") as f:
	f.write(" ".join(words))
