from sklearn.feature_extraction.text import TfidfVectorizer


class TermClassifier:

    def _tfidf(self, data=[]):
        """
        term weighting
        """
        vector = TfidfVectorizer()
        transformed = vector.fit_transform(data)

        return transformed.toarray()
