import json

from university.crawler.InvertedMongo import MongoInvertedIndex


def handle_scrapy_output(output_file):
    index = MongoInvertedIndex('wiki_index', 'index')
    with open(output_file, 'r') as file:
        data = json.load(file)
        for article in data:
            index.add_document(article['url'], article['content'])


handle_scrapy_output('wiki_scraper/output.json')
