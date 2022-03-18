# https://atcoder.jp/contests/abc127/tasks/abc127_b

r, D, x2000 = map(int, input().split())

x = [x2000] + [0] * 10

for i in range(1, 11):
  x[i] = r * x[i-1] - D
  print(x[i])