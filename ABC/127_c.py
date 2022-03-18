# https://atcoder.jp/contests/abc127/tasks/abc127_c

N, M = map(int, input().split())
L, R = [], []
for _ in range(M):
  l, r = map(int, input().split())
  L.append(l)
  R.append(r)

maxL = max(L)
minR = min(R)

# 該当する範囲がマイナスになる時は、0をansとする。
ans = max(minR-maxL+1, 0)
print(ans)
