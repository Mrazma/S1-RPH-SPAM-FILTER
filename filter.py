import os
import random
from typing import Counter
from corpus import Corpus
from trainingcorpus import TrainingCorpus
from tokens import tokenize
from utils import write_classification_to_file


class MyFilter:
    def __init__(self):
        self.spam_tag = "SPAM"
        self.ham_tag = "OK"

        # Holds Words and their values
        self.words = Counter()

        # Used to filter data
        self.bad_words = set()
        self.bad_count = 40 # Best combo so far 40 2
        self.bad_trigger_count = 2

        self.ham_strenght = 12

        self.min_word_len = 5

    def train(self, path):
        tc = TrainingCorpus(path)
        for fpath, fname, truth in tc.emails_paths():
            words, metadata, extra = tokenize(fpath)
            self._update_tables(words, metadata, extra, truth)

        self._finalize_training()

    def test(self, path):
        predictions = {}

        tc = Corpus(path)
        for fpath, fname in tc.emails_paths():
            words, metadata, extra = tokenize(fpath)
            prediction = self._predict(words, metadata, extra)
            predictions[fname] = prediction

        write_classification_to_file(os.path.join(path, "!prediction.txt"), predictions)

    # Updates tables used to predict mails later
    def _update_tables(self, words, metadata, extra, truth):
        filtered_words = Counter(
            {k: v for k, v in words.items() if len(k) >= self.min_word_len}
        )

        if truth == self.spam_tag:
            self.words += filtered_words
        if truth == self.ham_tag:
            scaled = Counter(
                {k: int(v * self.ham_strenght) for k, v in filtered_words.items()}
                )
            self.words = self.words - scaled

    def _finalize_training(self):
        self.bad_words = set(item for item, _ in self.words.most_common(self.bad_count))
        print(self.bad_words)

    # Predicts if spam or ham from tables
    def _predict(self, words: Counter, metadata, extra):
        words_set = set(item for item, _ in words.items())

        if len(self.bad_words & words_set) > self.bad_trigger_count:
            return self.spam_tag

        return self.ham_tag
