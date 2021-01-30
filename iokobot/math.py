import numpy as np

class BotMath:

    def _similarity(self, x = [], y = []):
        """
        calculate similarity between 2 vectors
        """
        a = np.array(x)
        b = np.array(y)
        
        penyebut = np.sum(a * b)
        pembilang = np.sqrt(np.sum(a**2)) * np.sqrt(np.sum(b**2))

        return penyebut / pembilang