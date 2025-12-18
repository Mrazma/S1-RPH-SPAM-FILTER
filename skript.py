from quality import compute_quality_for_corpus
from simplefilters import ParanoidFilter
import quality
import os

path = "data1"
path2 = "data2"
my_filter = ParanoidFilter()
my_filter.train(path2)
my_filter.test(path)

score = compute_quality_for_corpus(path)

print(f"Score of your filter is {score}.")

os.remove(f"{path}/!prediction.txt")
