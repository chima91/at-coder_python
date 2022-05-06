# https://atcoder.jp/contests/typical90/tasks/typical90_d

H, W = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]

column_sum = [0] * W
row_sum = [0] * H

for i in range(H):
  for j in range(W):
    column_sum[j] += A[i][j]
    row_sum[i] += A[i][j]

for i in range(H):
  ans = []
  for j in range(W):
    cross_sum = row_sum[i] + column_sum[j] - A[i][j]
    ans.append(cross_sum)
  print(*ans)
