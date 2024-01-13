# from afinn import Afinn
import pickle

# afinn = Afinn()



import nltk
nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

pickle.dump(sia, open("model.pkl", "wb"))
