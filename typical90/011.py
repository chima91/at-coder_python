N = int(input())
tasks = [tuple(map(int, input().split())) for _ in range(N)]
tasks.sort(key=lambda x: x[0])

dp = [[0] * 5002 for _ in range(N+1)]

for i in range(N):
  di, ci, si = tasks[i]
  for j in range(1, 5002):
    dp[i+1][j] = max(dp[i+1][j], dp[i+1][j-1], dp[i][j])
    if j-1 <= di and j-ci >= 1:
      dp[i+1][j] = max(dp[i+1][j], dp[i][j-ci] + si)

print(dp[N][5001])