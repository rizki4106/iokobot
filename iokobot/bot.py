from sklearn.feature_extraction.text import TfidfVectorizer
from .math import BotMath
import pandas as pd

class BotBody(BotMath):

    def __init__(self):
        self.questions = []
        self.answers = []
        self.score_value = 0

    def fit(self, data = ""):
        """
        fit training data
        """
        data = pd.read_csv(data)
        self.questions = data.iloc[:, 0]
        self.answers = data.iloc[:, -1]

    def predict(self, questions = ''):
        """
        predict new questions used for, ask the bot about the answer
        """
        pred_data =  self.questions.append(pd.Series([questions]), ignore_index=True)

        # get the answer
        return self.__get_answer(questions=pred_data)

    def __get_answer(self, questions = []):
        """
        get the answer by calculating text similarity based on tf-idf
        """

        vector = TfidfVectorizer()
        t_questions = vector.fit_transform(questions).toarray()

        # calculate similarity
        similarity = []
        for i in range(0, len(t_questions) - 1):
            similarity.append(self._similarity(t_questions[len(t_questions) - 1], t_questions[i]))
        
        # get index array of max value similarity
        index = similarity.index(max(similarity))

        # return the answer
        self.score_value = max(similarity)
        return self.answers.values[index]

    def score(self):
        """
        return the similarity score
        """

        return self.score_value