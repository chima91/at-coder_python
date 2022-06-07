from math import atan2, degrees

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for p, (x0, y0) in enumerate(XY):
  deg = [degrees(atan2(y-y0, x-x0)) for q, (x, y) in enumerate(XY) if p != q]
  deg.sort()

  i, j = 1, 0
  while i < N-1:
    ans = max(ans, 180-abs(deg[j]+180-deg[i]))
    if deg[i]-deg[j] < 180: i += 1
    else: j += 1

print(ans)