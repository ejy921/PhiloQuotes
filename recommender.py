import numpy as np
from sklearn.neighbors import NearestNeighbors

class RecommenderSystem:
    def __init__(self, quote_dataset, user_profile):
        self.quote_dataset = quote_dataset
        self.user_profile = user_profile

        # adjust as needed
        self.knn_model = NearestNeighbors(n_neighbors=5, metric='cosine')
        self.fit_model()

    def fit_model(self):
        feature_vectors = self.quote_dataset.feature_vectors
        self.knn_model.fit(feature_vectors)
        
    # recommends based on user profile
    def recommend(self, top_n=5):
        # vectorized form, reshape to 2d array suited for knn model
        user_vector = self.user_profile.profile_vector.reshape(1, -1)

        # Get the top N similar quotes based on cosine similarity
        distances, indices = self.knn_model.kneighbors(user_vector, n_neighbors=top_n)

        recommendations = []
        for i in indices[0]:
            quote = self.quote_dataset[i]
            recommendations.append((quote.quote_text, distances[0][i])) # include distance between user and quote for context
        
        return recommendations
    
    def update_with_feedback(self, quote_i, feedback):
        # get feedback based on quote
        quote_vector = self.quote_dataset.features_vectors[quote_i]
        self.user_profile.update_profile(quote_vector, feedback)




