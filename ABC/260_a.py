import collections

S = list(input())

c = collections.Counter(S)

for item in c.items():
  if item[1] == 1:
    print(item[0])
    exit()

print(-1)