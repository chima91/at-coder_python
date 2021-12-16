from collections import Counter

S = input()

if Counter(list(S)).most_common()[0][1] == 3:
    print(1)
elif Counter(list(S)).most_common()[0][1] == 2:
    print(3)
else:
    print(6)
