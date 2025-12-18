from corpus import Corpus
import os
from utils import read_classification_from_file

HAM_TAG = "OK"
SPAM_TAG = "SPAM"

class TrainingCorpus(Corpus):
    def __init__(self, path):
        super().__init__(path)
        
        self.truth = read_classification_from_file(
            os.path.join(path,"!truth.txt"))


    def get_class(self,mail_filename):
        if mail_filename not in self.truth.keys():
            raise ValueError

        return self.truth[mail_filename]
    
    def is_ham(self, mail_filename):
        return self.get_class(mail_filename) == HAM_TAG
    
    def is_spam(self, mail_filename):
        return self.get_class(mail_filename) == SPAM_TAG
    
    def emails(self):
        for fname, body in super().emails():
            yield fname, body, self.get_class(fname)
