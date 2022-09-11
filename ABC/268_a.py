import collections

l = list(map(int, input().split()))

ans = collections.Counter(l)

print(len(ans))

# 別解
# print(len(set(list(map(int, input().split())))))
