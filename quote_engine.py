import numpy as np

from features import central_characteristics, other_characteristics, central_philosophies, other_philosophies

class Quote:
    def __init__(self, quote_text, philosophy, characteristics):
        self.quote_text = quote_text
        self.characteristics = characteristics.split(',') if characteristics else []
        self.philosophy = philosophy.split(',') if philosophy else [] # ensure that it's a list

    def __repr__(self):
        return f"Quote({self.quote_text})"

class QuoteDataset:
    def __init__(self, quotes):
        self.quotes = quotes
        self.feature_vectors = self.create_feature_vectors()

    def create_feature_vectors(self):
        feature_vectors = []
        for quote in self.quotes:
            # make feature vector with len of central characteristics + schools
            feature_vector = np.zeros(len(central_characteristics) + len(central_philosophies))

            # process characteristics
            for char in quote.characteristics:
                if char in central_characteristics:
                    index = central_characteristics.index(char)
                    feature_vector[index] += 1
                if char in other_characteristics:
                    char_vector = np.array(other_characteristics[char])
                    feature_vector[:len(central_characteristics)] += char_vector

            # process schools
            for philosophy in quote.philosophy:
                if philosophy in central_philosophies:
                    index = len(central_characteristics) + central_philosophies.index(philosophy)
                    feature_vector[index] += 1
                if philosophy in other_philosophies:
                    philosophy_vector = np.array(other_philosophies[philosophy])
                    feature_vector[len(central_characteristics):] += philosophy_vector

            feature_vectors.append(feature_vector)

        return np.array(feature_vectors)
