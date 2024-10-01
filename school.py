import json5
import numpy as np
from sklearn.neighbors import NearestNeighbors

class School:
  schools = [
    "Stoicism", "Mysticism", "Existentialism", "Classical Greek",
    "Transcendentalism", "Rationalism", "Empiricism"
  ]

  central_schools = ["Existentialism", "Rationalism", "Classical Greek"]

  other_schools = {
    "Mysticism": [1, 0, 1],               # Existentialism and Classical Greek
    "Transcendentalism": [0, 1, 1],       # Rationalism and Classical Greek
    "Stoicism": [1, 1, 0],                # Existentialism and Rationalism
    "Empiricism": [1, 1, 1]               # All three
  }

  def __init__(self):
    self.feature_vectors = []  # Initialize feature_vectors list
    self.quote_texts = []       # Initialize quote_texts list
    
    with open('quotes.json', 'r') as f:
      quotes_data = json5.load(f)

    # Iteration over each quote
    for quote in quotes_data:
      feature_vector = [0] * len(self.central_schools)

      if 'philosophy' in quote:
        philosophy = quote['philosophy'].split(',')
        for char in philosophy:
          char = char.strip()  # Clean up whitespace
          if char in self.central_schools:
            index = self.central_schools.index(char)
            feature_vector[index] += 1
          
          if char in self.other_schools:
            feature_vector = np.add(feature_vector, self.other_schools[char])

        self.feature_vectors.append(np.array(feature_vector))
        self.quote_texts.append(quote['quote'])

    self.feature_vectors = np.array(self.feature_vectors)

  def display_feature_vectors(self):
    print("Feature Vectors")
    for text, vector in zip(self.quote_texts, self.feature_vectors):
      print(f"Quote: {text}\nFeature Vector: {vector}\n")

# Example usage
school = School()
school.display_feature_vectors()
