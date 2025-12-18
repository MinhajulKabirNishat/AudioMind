import nltk
from collections import Counter
import string

nltk.download('punkt')

with open("text/output.txt", "r", encoding="utf-8") as f:
    text = f.read()

sentences = nltk.sent_tokenize(text)
words = nltk.word_tokenize(text.lower())
words = [w for w in words if w not in string.punctuation]

print("Text Analysis Results")
print("--------------------")
print("Characters:", len(text))
print("Words:", len(words))
print("Sentences:", len(sentences))

freq = Counter(words).most_common(5)
print("Most Frequent Words:")
for word, count in freq:
    print(word, ":", count)
