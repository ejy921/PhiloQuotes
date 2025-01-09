import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from quote_engine import Quote, QuoteDataset
from user import UserProfile
from recommender import RecommenderSystem

print("Current dir: ", os.getcwd())

# load quotes into array
quotes = QuoteDataset.load_quotes('quotes.json')

# initialize quote dataset
quote_dataset = QuoteDataset(quotes)
# initialize user 
user = UserProfile()
# initialize recommender
recommender = RecommenderSystem(quote_dataset, user)

recommender.fit_model()

# Run a recommender loop
for recommendation in recommender.recommend(top_n=len(quote_dataset.quotes)):
    quote_text, quote_source, quote_philosophy, quote_chars, distance = recommendation
    print(f"\nRecommendation: {quote_text}\nPhilosopher: {quote_source}\nPhilosophy: {quote_philosophy}\nCharacteristics: {quote_chars}\n")
    print(f"(Similarity: {distance:.2f})")

    feedback = input("Quote feedback:").strip().lower()

    if feedback == "quit":
        print("Goodbye, have a nice day")
        break
    elif feedback == "like":
        # find current quote by finding matching quote in dataset
        quote = next((q for q in quote_dataset.quotes if q.quote_text == quote_text), None)
        if quote:
            # find vector for current quote and update profile
            quote_vector = quote_dataset.feature_vectors[quote_dataset.quotes.index(quote)]
            recommender.user_profile.update_profile(quote_vector, feedback_type='like')
            print("Liked")
        else:
            print("Error: quote not found.")
    elif feedback == "dislike":
        quote = next((q for q in quote_dataset.quotes if q.quote_text == quote_text), None)
        if quote:
            quote_vector = quote_dataset.feature_vectors[quote_dataset.quotes.index(quote)]
            recommender.user_profile.update_profile(quote_vector, feedback_type='dislike')
            print("Disliked")
        else:
            print("Error: quote not found.")
    else:
        print("Please type either like, dislike, or quit.")


