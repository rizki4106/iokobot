import numpy as np
import re
import string

class TermClassifier:

    def _tfidf(self, data = []):
        """
        term weighting
        """
        doc = []

        # remove punctuation
        for text in data:
            doc.append(self.__remove_punctuation(text).lower())

        # extract unique features

        bow = []
        features = ''
        for i in doc:
            for word in i.split(" "):
                features += word + " "
                if word not in bow and word != '':
                    bow.append(word)

        
        # calculate tfidf
        matrix = []
        for document in doc:
            arr = []
            for word in bow:
                tf = len(re.findall(word, document)) / len(bow)
                idf = np.log(1 + len(doc) / 1 + len(re.findall(word, features))) + 1
                
                # normalization matrix
                tfidf = (tf * idf)**2
                arr.append(np.sqrt(tfidf))
            matrix.append(arr)

        return np.array(matrix)

    def __remove_punctuation(self, words):
        """
        remove punctuation ?~!@#$%^
        """
        
        clean_str = words.lower()
        for pct in string.punctuation:
            clean_str = clean_str.replace(pct, "")

        # remove space on the last words
        return clean_str