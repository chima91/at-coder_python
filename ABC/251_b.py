N, W = map(int, input().split())
A = list(map(int, input().split())) + [0,0]

from itertools import combinations
S = set()
for x,y,z in combinations(A, 3):
  C = x+y+z
  if C <= W:
    S.add(C)
print(len(S))
