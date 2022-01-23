# https://atcoder.jp/contests/abc178/tasks/abc178_d

S = int(input())
mod = 10**9 + 7

# [0] * 2001で十分だがインデックスエラーなどの余計なミスが起きないようにする
dp = [0] * (10**5)
dp[0] = 0
dp[1] = 0
dp[2] = 0
dp[3] = 1
dp[4] = 1
dp[5] = 1

for i in range(6, S+1):
    dp[i] = sum(dp[:i-2]) + 1
    dp[i] %= mod

print(dp[S])
