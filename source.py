import json5
import numpy as np

QUOTENUM = 128 # Number of quotes in json file.

# Load the quotes data from the JSON file
# List of all the characteristics
characteristics = [
    "Analytical", "Inquisitive", "Modern", "Pragmatic", "Empathetic", 
    "Skeptical", "Introspective", "Philosophical", "Visionary", "Creative", 
    "Spiritual", "Challenging", "Hopeful", "Uplifting"
]

central_characteristics = ["Analytical", "Empathetic", "Visionary"]

other_characteristics = {
    "Inquisitive": [1, 0, 1],
    "Modern": [1, 0, 1],
    "Pragmatic": [1, 1, 0],
    "Skeptical": [1, 0, 0],
    "Introspective": [1, 1, 0],
    "Philosophical": [1, 1, 0],
    "Creative": [0, 0, 1],
    "Spiritual": [0, 1, 1],
    "Challenging": [1, 0, 1],
    "Hopeful": [0, 1, 1],
    "Uplifting": [0, 1, 0],
}

# Attributes of each Quote object
class Quote:
  def __init__(self, source, philosophy, quote_text, characteristics):
    self.source = source
    self.philosophy = philosophy
    self.quote_text = quote_text
    self.characteristics = characteristics.split(',') if characteristics else []

  def __repr__(self):
    return f"Quote({self.quote_text})"


class QuoteDataset:
  def __init__(self):
    self.quotes = []
    self.central_characteristics = central_characteristics
    self.other_characteristics = other_characteristics

  # load quotes in self.quotes array as Quote objects
  def load_quotes(self):
    with open('quotes.json', 'r') as f:
        quotes_data = json5.load(f)
        for item in quotes_data:
          quote = Quote(
            source=item['source'],
            philosophy=item['philosophy'],
            quote_text=item['quote'],
            characteristics=item['characteristic']
          )
          self.quotes.append(quote)
  
  def feature_vectors(self):
    feature_vectors = []
    for quote in self.quotes:
        # initialize feature vector containing zeros
        feature_vector = [0] * len(self.central_characteristics)

        # count for central characteristics
        for char in quote.characteristics:
          if char in self.central_characteristics:
            index = self.central_characteristics.index(char)
            feature_vector[index] += 1

          if char in self.other_characteristics:
            feature_vector += np.array(self.other_characteristics[char])
        
        feature_vectors.append(feature_vector)

    return np.array(feature_vectors)

quote_dataset = QuoteDataset()
quote_dataset.load_quotes('quotes.json')
feature_vectors = quote_dataset.feature_vectors()

for quote, vector in zip(quote_dataset.quotes, feature_vectors):
  print(f"Quote: {quote.quote_text}\nFeature Vector: {vector}\n")

# Initialize likes/dislikes for each quote
likes_dislikes = {quote['_id']: {'rating': 0} for quote in quote_dataset}

def like(item):
  if item in likes_dislikes:
    likes_dislikes[item]['rating'] += 1
  else:
    print(f"Item '{item}' not found.")

def dislike(item):
  if item in likes_dislikes:
    likes_dislikes[item]['rating'] -= 1
  else:
    print(f"Item '{item}' not found.")

# # Print the current state
# print(QUOTENUM)