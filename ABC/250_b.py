# https://atcoder.jp/contests/abc250/tasks/abc250_b

N, A, B = map(int, input().split())

field = [['.'] * (N*B) for _ in range(N*A)]

for i in range(N*A):
  for j in range(N*B):
    if ((i // A) + (j // B)) % 2 == 1:
      field[i][j] = '#'

for row in field:
  print(''.join(row))