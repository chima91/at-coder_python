N = int(input())

a = [[1] * (i+1) for i in range(N)]

for i in range(N):
  a[i][0] = 1
  a[i][i] = 1
  for j in range(1, i):
    a[i][j] = a[i-1][j-1] + a[i-1][j]
  print(*a[i])