
from filter import MyFilter
import quality

path1 = r"data\1"
path2 = r"data\2"

print("---- Trained on 1 ------")

filter = MyFilter()
filter.train(path1)
filter.test(path1)
filter.test(path2) 

print("1:",quality.get_quality_for_corpus(path1))
print("2:",quality.get_quality_for_corpus(path2))

print("---- Trained on 2 ------")

filter = MyFilter()
filter.train(path2)
filter.test(path1)
filter.test(path2)

print("1:",quality.get_quality_for_corpus(path1))
print("2:",quality.get_quality_for_corpus(path2))