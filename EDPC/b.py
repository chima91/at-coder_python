# https://atcoder.jp/contests/dp/tasks/dp_b

N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [0] * N
dp[0] = 0

for i in range(1, N):
  dp[i] = 10 ** 18
  for j in range(1, K+1):
    if i-j >= 0:
      dp[i] = min(dp[i], dp[i-j] + abs(h[i] - h[i-j]))

print(dp[N-1])
