# https://atcoder.jp/contests/abc242/tasks/abc242_c

mod = 998244353
N = int(input())

dp = [[0] * 9 for _ in range(N+1)]
dp[0] = [1] * 9

for i in range(1, N):
  for d in range(9):
    # 1つ前の桁の数が1小さい
    if d-1 >= 0:
      dp[i][d] += dp[i-1][d-1]
    # 1つ前の桁の数と同じ
    dp[i][d] += dp[i-1][d]
    # 1つ前の桁の数が1大きい
    if d+1 < 9:
      dp[i][d] += dp[i-1][d+1]

    dp[i][d] %= mod

print(sum(dp[N-1]) % mod)