def solve(l, r):
  if r - l < l:
    return 0
  n = r - 2*l + 1
  return n * (n+1) // 2

t = int(input())

for _ in range(t):
  l, r = map(int, input().split())
  print(solve(l, r))