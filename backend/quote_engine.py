import numpy as np
import json
from features import Features 

class Quote:
    def __init__(self, quote_text, source, philosophy, characteristics):
        self.quote_text = quote_text
        self.source = source
        self.characteristics = characteristics.split(',') if characteristics else []
        self.philosophy = philosophy.split(',') if philosophy else [] # ensure that it's a list

    def __repr__(self):
        return f"Quote({self.quote_text})"

class QuoteDataset:
    def __init__(self, quotes):
        self.quotes = quotes
        self.feature_vectors = self.create_feature_vectors()

    def load_quotes(filepath):
        with open(filepath, 'r') as file:
            data = json.load(file)
        quotes = []
        for item in data:
            quotes.append(Quote(
                quote_text=item['quote'],
                source = item.get('source', ''), # if doesn't exist, return empty str
                characteristics=item.get('characteristic', ''), 
                philosophy=item.get('philosophy', '')
            ))
        return quotes

    def create_feature_vectors(self):
        feature_vectors = []
        for quote in self.quotes:
            # make feature vector with len of central characteristics + schools
            feature_vector = np.zeros(len(Features.central_characteristics) + len(Features.central_philosophies))

            # process characteristics
            for char in quote.characteristics:
                if char in Features.central_characteristics:
                    index = Features.central_characteristics.index(char)
                    feature_vector[index] += 1
                if char in Features.other_characteristics:
                    char_vector = np.array(Features.other_characteristics[char])
                    feature_vector[:len(Features.central_characteristics)] += char_vector

            # process schools
            for philosophy in quote.philosophy:
                if philosophy in Features.central_philosophies:
                    index = len(Features.central_characteristics) + Features.central_philosophies.index(philosophy)
                    feature_vector[index] += 1
                if philosophy in Features.other_philosophies:
                    philosophy_vector = np.array(Features.other_philosophies[philosophy])
                    feature_vector[len(Features.central_characteristics):] += philosophy_vector

            feature_vectors.append(feature_vector)

        return np.array(feature_vectors)
