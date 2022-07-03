N, Q = map(int, input().split())
S = list(input())

start = 0
for _ in range(Q):
  t, x = map(int, input().split())
  if t == 1:
    start = (start - x) % N
  else:
    x -= 1
    print(S[(start + x) % N])