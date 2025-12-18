from corpus import Corpus

class BaseFilter:
    def __init__(self):
        self.spam_tag = "SPAM"
        self.ham_tag = "OK"

    def train(self, path):
        pass

    def predict(self):
        return None

    def test(self, path):
        my_corpus = Corpus(path)
        with open(f"{path}/!prediction.txt", 'w', encoding='utf-8') as file:
            for f, inside in my_corpus.emails():
                file.write(f"{f} {self.predict()}\n")