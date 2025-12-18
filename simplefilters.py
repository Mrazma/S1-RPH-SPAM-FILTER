from basefilter import  BaseFilter
import random

class NaiveFilter(BaseFilter):
    def predict(self):
        return self.ham_tag


class ParanoidFilter(BaseFilter):
    def predict(self):
        return self.spam_tag

class RandomFilter(BaseFilter):
    def predict(self):
        answer = random.choice([self.spam_tag, self.ham_tag])
        return answer
