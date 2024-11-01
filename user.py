import numpy as np

class UserProfile:
  def __init__(self, central_schools, default_preferences=None):
    # self.central_schools = central_schools
    self.pref_vector = np.zeros(len(central_schools))

  def like(self, quote_features):
    self.pref_vector += quote_features