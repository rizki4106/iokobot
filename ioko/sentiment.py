from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd


class SentimentAnalysis:

    def predict(self, data=[]):
        """
        predicting sentiment analysis
        """
        data = pd.read_csv("data/training_data.csv")

        # tfidf vectorizer
        vector = TfidfVectorizer(smooth_idf=True)
        x = vector.fit_transform(data['content'].values).toarray()
        y = data['sentiment'].values

        # fit training data
        algorithm = MultinomialNB()
        algorithm.fit(x, y)

        # try to predict sentiment analysis
        return algorithm.predict(vector.transform(data).toarray())[0]
