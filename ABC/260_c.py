N, X, Y = map(int, input().split())

red = [0] * (N+1)
blue = [0] * (N+1)

red[N] = 1

for i in range(N, 1, -1):
  cnt = red[i]
  red[i-1] += cnt
  blue[i] += cnt * X

  cnt = blue[i]
  red[i-1] += cnt
  blue[i-1] += cnt * Y

print(blue[1])