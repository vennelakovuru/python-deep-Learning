# importing Natural Language Toolkit and required libraries
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk import ne_chunk, ngrams
from nltk.tag import pos_tag

nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('punkt')

# Reading the data in the file
input = open('input.txt', encoding="utf8").read()

# Tokenizing into Sentences and Words
sentence_tokens = nltk.sent_tokenize(input)  # Sentence Tokens
word_tokens = nltk.word_tokenize(input)  # Words Tokens

print("\nSentence Tokens:\n", sentence_tokens)
print("\n\nWord Tokens:\n", word_tokens)

# performing Part of Speech tagging using pos_tag
pos = nltk.pos_tag(sentence_tokens)
print("\n\nPart of Speech tagging:\n", pos)

# Stemming

# PorterStemmer
porterStemmer = PorterStemmer()
print("\n\nPorter Stemmer:\n")
for i in sentence_tokens:
    print(porterStemmer.stem(i), end='')

# LancasterStemmer
LancasterStemmer = LancasterStemmer()
print("\n\nLancaster Stemmer:\n")
for i in sentence_tokens:
    print(LancasterStemmer.stem(i), end='')

# SnowballStemmer
SnowballStemmer = SnowballStemmer('english')
print("\n\nSnowball Stemmer:\n")
for i in sentence_tokens:
    print(SnowballStemmer.stem(i), end='')

# Lemmatization

# Applying Lemmatization using WordNetLemmatizer
Lemmatization = WordNetLemmatizer()
print('\n\nLemmatization:\n')
for i in sentence_tokens:
    print(Lemmatization.lemmatize(i), end=' ')

# Trigram
print("\n\nTrigram:\n")
token = nltk.word_tokenize(input)
n = 0
for s in sentence_tokens:
    n = n + 1
    if n < 2:
        token = nltk.word_tokenize(s)
        bigram = list(ngrams(token, 2))
        trigram = list(ngrams(token, 3))
        print("The text:", s, "\nword_tokenize:", token, "\nbigrams:", bigram, "\ntrigrams", trigram)

# Named Entity Recognition
print("\n\nNamed Entity Recognition:\n")
n = 0
for s in sentence_tokens:
    n = n + 1
    if n < 2:
        print(ne_chunk(pos_tag(nltk.word_tokenize(s))))
