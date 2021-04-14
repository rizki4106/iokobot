from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ContentBased:

    training = []
    _score = []

    def fit(self, data=[]):
        """
        fit training data
        """
        self.training = data

    def predict(self, y=[]):
        """
        predict recommendation
        """
        return self.__calculate(training=self.training, testing=y)

    def __calculate(self, training=[], testing=''):
        """
        predict similarity
        """

        vector = TfidfVectorizer()

        # training data to numerical vector
        x = vector.fit_transform(training).toarray()

        # testing data to numerical vector
        y = vector.transform([testing]).toarray()

        # calculate similarity
        similarity = []

        for i in range(len(training)):
            similarity.append(cosine_similarity(
                x[i].reshape(1, -1), y.reshape(1, -1))[0][0])

        # copy similarity
        copy_similarity = [i for i in similarity]
        copy_similarity.sort(reverse=True)

        # index array of recommendation
        recommendation = [similarity.index(i) for i in copy_similarity]

        # set similarity score to global variable
        self._score = [
            similarity[similarity.index(i)] for i in copy_similarity]

        return recommendation

    def score(self):
        """
        get similarity score
        """

        return self._score
