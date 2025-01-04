import json


class InvertedIndex:
    def __init__(self):
        self.index = {}

    def add_document(self, document_id, text):
        words = text.split()
        for word in words:
            if word not in self.index:
                self.index[word] = []
            if document_id not in self.index[word]:
                self.index[word].append(document_id)

    def search(self, word):
        return self.index.get(word, [])


with open('wiki_scraper/output.json', 'r') as file:
    document_list: list[dict] = json.load(file)
documents = {}
for doc in document_list:
    documents[doc.get('id')] = doc.get('content')


index = InvertedIndex()
for doc_id, content in documents.items():
    index.add_document(doc_id, content)

print(index.search('2006'))
