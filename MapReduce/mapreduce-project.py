from collections import Counter

print("please insert your List for Mapping with a ',' among each one :")

userInput = input()
mappingList = userInput.split(",")
reducePhase = Counter(mappingList)
dictReducePhase = dict(reducePhase)
print(dictReducePhase)
merged = dictReducePhase.items()
print()
for i, j in merged:
    print("{0} key = {1} values".format(i, j))

