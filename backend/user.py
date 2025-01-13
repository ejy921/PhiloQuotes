import numpy as np

from features import Features 

class UserProfile:
  def __init__(self, initial_preferences=None):
    self.profile_vector = np.zeros(len(Features.central_characteristics) + len(Features.central_philosophies)) if initial_preferences is None else initial_preferences

  def get_profile(self):
    return self.profile_vector

  def update_profile(self, quote_vector, feedback_type):
    if feedback_type == 'like':
      self.profile_vector += quote_vector # increase influence of this quote's features
    elif feedback_type == 'dislike':
      self.profile_vector -= quote_vector

    # Optional: Normalize the profile vector to prevent extreme values
    self.profile_vector = np.clip(self.profile_vector, 0, 1)