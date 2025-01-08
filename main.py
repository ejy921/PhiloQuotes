from quote_engine import Quote, QuoteDataset
from user import UserProfile
from recommender import RecommenderSystem

import os

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
    quote_text, distance = recommendation
    print(f"\nRecommendation: {quote_text}\n(Similarity: {distance:.2f})")

    feedback = input("Quote feedback:").strip().lower()

    if feedback == "quit":
        print("Goodbye, have a nice day")
        break
    elif feedback == "yes":
        # find vector for current quote
        quote_vector = quote_dataset.feature_vectors[quote_dataset.quotes.index(Quote(quote_text, '', ''))]
        recommender.user_profile.update_profile(quote_vector, feedback_type='like')
        print("Liked")
    elif feedback == "no":
        quote_vector = quote_dataset.feature_vectors[quote_dataset.quotes.index(Quote(quote_text, '', ''))]
        recommender.user_profile.update_profile(quote_vector, feedback_type='dislike')
        print("Disliked")
    else:
        print("Please type either yes, no, or quit.")


