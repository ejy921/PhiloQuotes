import json5
from sklearn.neighbors import NearestNeighbors
import numpy as np

characteristics = [
    "Analytical", "Inquisitive", "Modern", "Pragmatic", "Empathetic", 
    "Skeptical", "Introspective", "Philosophical", "Visionary", "Creative", 
    "Spiritual", "Challenging", "Hopeful", "Uplifting"
]

with open('quotes.json', 'r') as f:
  quotes_data = json5.load(f)



  