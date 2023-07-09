from collections import Counter
from statistics import mean
words = input()

print("Total Number of Words: ", len(words))

split_it = words.split()
Counter = Counter(split_it)
mostCommon = Counter.most_common(3)
print("Most Common Word: ", mostCommon)


long = max(words, key=len)
result = [i for i in long if len(words) == long]
print(result)

meanWord = mean(len(word) for word in words.split())
print("Average", meanWord)