from collections import Counter

import matplotlib
import matplotlib.pyplot as plt
from pymongo import MongoClient

matplotlib.use("MacOSX")
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']
collection = db['your_collection']

documents = collection.find()

all_text = " ".join(doc['text_field'] for doc in documents if 'text_field' in doc)


words = all_text.lower().replace('.', '').replace(',', '').split()

word_counts = Counter(words)

most_common_words = word_counts.most_common(10)
words, frequencies = zip(*most_common_words)

plt.figure(figsize=(10, 5))
plt.bar(words, frequencies, color='skyblue')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 10 Most Frequent Words in Text')
plt.xticks(rotation=45)
plt.show()
