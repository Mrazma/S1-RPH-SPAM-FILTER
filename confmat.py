class BinaryConfusionMatrix:
    def __init__(self, pos_tag="SPAM", neg_tag="OK"):
        self.pos_tag = pos_tag
        self.neg_tag = neg_tag

        self.stats = {"tp": 0, "tn": 0, "fp": 0, "fn": 0}

    def as_dict(self):
        return self.stats

    def update(self, truth, prediction):
        # Check if values are valid
        self._valid_value_check(truth)
        self._valid_value_check(prediction)

        # Increment based on correctness
        if truth == prediction:
            if prediction == self.pos_tag:
                self.stats["tp"] += 1
            else:
                self.stats["tn"] += 1
        else:
            if prediction == self.pos_tag:
                self.stats["fp"] += 1
            else:
                self.stats["fn"] += 1

    def compute_from_dicts(self, truth_dict: dict, pred_dict: dict):
        # Check if the dictionaries have the same items
        if truth_dict.keys() != pred_dict.keys():
            raise ValueError

        # Processes the dictionaries
        for name, tag in truth_dict.items():
            self.update(tag, pred_dict[name])

    def _valid_value_check(self, value):
        if value not in [self.neg_tag, self.pos_tag]:
            raise ValueError