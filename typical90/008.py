N = int(input())
S = input()

atcoder = 'atcoder'
MOD = 10 ** 9 + 7

dp = [[0] * 8 for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
  for j in range(8):
    dp[i+1][j] += dp[i][j]
    dp[i+1][j] %= MOD
    if j < len(atcoder) and S[i] == atcoder[j]:
      dp[i+1][j+1] += dp[i][j]
      dp[i+1][j+1] %= MOD

print(dp[N][len(atcoder)])