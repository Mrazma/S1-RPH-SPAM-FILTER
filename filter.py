import os
from corpus import Corpus
from trainingcorpus import TrainingCorpus
from tokens import tokenize
from utils import write_classification_to_file


class MyFilter:
    def __init__(self):
        self.spam_tag = "SPAM"
        self.ham_tag = "OK"

        self.spam_words = None
        self.ham_words = None

        self.spam_hashes = None

    def train(self, path):
        tc = TrainingCorpus(path)
        for fpath, fname, truth in tc.emails_paths():
            words, metadata, extra = tokenize(fpath)
            self._update_tables(words, metadata, extra, truth)

    def test(self, path):
        predictions = {}

        tc = Corpus(path)
        for fpath, fname in tc.emails_paths():
            words, metadata, extra = tokenize(fpath)
            prediction = self._predict(words, metadata, extra)
            predictions[fname] = prediction

        write_classification_to_file(
            os.path.join(path, "!prediction.txt"), predictions
        )

    # Updates tables used to predict mails later
    def _update_tables(self, words, metadata, extra, truth): ...

    # Predicts if spam or ham from table
    def _predict(self, words, metadata, extra):
        return self.spam_tag
