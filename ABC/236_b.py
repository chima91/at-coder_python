import collections

N = int(input())
A = list(map(int, input().split()))

a = collections.Counter(A)
print(a.most_common()[-1][0])
