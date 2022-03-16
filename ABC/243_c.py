# https://atcoder.jp/contests/abc243/tasks/abc243_c

N = int(input())

row = {}

for i in range(N):
  x, y = map(int, input().split())
  if y not in row:
    row[y] = []
  row[y].append((x, i))

S = input()

INF = 10 ** 18

for y in row:
  Rmin = INF
  Lmax = -INF
  for x, i in row[y]:
    if S[i] == 'R':
      Rmin = min(Rmin, x)
    if S[i] == 'L':
      Lmax = max(Lmax, x)
  if Rmin <= Lmax:
    print('Yes')
    exit()

print('No')