# https://atcoder.jp/contests/abc153/tasks/abc153_e

H, N = map(int, input().split())

# 初期値は十分に大きい数
dp = [10**10]*(H+1)
dp[0] = 0

# 表の小さいほうから答えに辿り着くまで埋める
for i in range(N):
    A, B = map(int, input().split())
    for h in range(H+1):
        if h+A <= H:
            dp[h+A] = min(dp[h+A], dp[h]+B)
        else:
            dp[H] = min(dp[H], dp[h]+B)

print(dp[H])
