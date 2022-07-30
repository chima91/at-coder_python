import sys
sys.setrecursionlimit(10 ** 7)

par = [-1] * (2002 * 2002)

def root(x):
  if par[x] < 0:
    return x
  else:
    par[x] = root(par[x])
    return par[x]

def unite(x, y):
  x = root(x)
  y = root(y)
  if x == y:
    return
  par[x] += par[y]
  par[y] = x

def ind(x, y):
  return 2002 * x + y

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

H, W = map(int, input().split())
Q = int(input())

red = [[False] * (W+2) for _ in range(H+2)]

for _ in range(Q):
  q = list(map(int, input().split()))
  if q[0] == 1:
    r, c = q[1:]
    red[r][c] = True
    for d in range(4):
      nx = r + dx[d]
      ny = c + dy[d]
      if not red[nx][ny]: continue
      unite(ind(r, c), ind(nx, ny))
  else:
    ra, ca, rb, cb = q[1:]
    if red[ra][ca] and red[rb][cb] and root(ind(ra, ca)) == root(ind(rb, cb)):
      print("Yes")
    else:
      print("No")