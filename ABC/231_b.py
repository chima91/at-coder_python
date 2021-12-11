from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

print(Counter(S).most_common()[0][0])
