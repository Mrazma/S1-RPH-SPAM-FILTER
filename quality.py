import os
import utils
from confmat import BinaryConfusionMatrix as BCM

def quality_score(tp, tn, fp, fn):
    return (tp + tn) / (tp + tn + 10 * fp + fn)


def compute_quality_for_corpus(corpus_dir):
    # Load dictionaries
    truth = utils.read_classification_from_file(os.path.join(corpus_dir, "!truth.txt"))
    predictions = utils.read_classification_from_file(
        os.path.join(corpus_dir, "!prediction.txt")
    )
    
    # Creates BinaryConfusion Matrix
    matrix = BCM()

    # Gets the values
    matrix.compute_from_dicts(truth, predictions)
    values = matrix.as_dict()

    return quality_score(values["tp"], values["tn"], values["fp"], values["fn"])

## Returns quality and values
def get_quality_for_corpus(corpus_dir):
    # Load dictionaries
    truth = utils.read_classification_from_file(os.path.join(corpus_dir, "!truth.txt"))
    predictions = utils.read_classification_from_file(
        os.path.join(corpus_dir, "!prediction.txt")
    )
    
    # Creates BinaryConfusion Matrix
    matrix = BCM()

    # Gets the values
    matrix.compute_from_dicts(truth, predictions)
    values = matrix.as_dict()

    return quality_score(values["tp"], values["tn"], values["fp"], values["fn"]), values
