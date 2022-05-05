# https://atcoder.jp/contests/typical90/tasks/typical90_c

import sys
# print(sys.getrecursionlimit())
sys.setrecursionlimit(10 ** 6)

N = int(input())

edges = [[] for _ in range(N)]

for _ in range(N-1):
  A, B = map(int, input().split())
  # A, Bを0インデックスにする
  A -= 1
  B -= 1
  edges[A].append(B)
  edges[B].append(A)

dist = [0] * N

def dfs(x, last=-1):
  global dist
  for to in edges[x]:
    if to == last:
      continue
    dist[to] = dist[x] + 1
    dfs(to, x)

dfs(0)
max_dist = max(dist)
farest = dist.index(max_dist)

dist[farest] = 0
dfs(farest)

print(max(dist) + 1)