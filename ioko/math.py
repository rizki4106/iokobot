from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class BotMath:

    def _similarity(self, x=[], y=[]):
        """
        calculate similarity between 2 vectors
        """
        a = np.array(x)
        b = np.array(y)

        return cosine_similarity(a.reshape(1, -1), b.reshape(1, -1))[0]
