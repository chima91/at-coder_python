# https://atcoder.jp/contests/abc178/tasks/abc178_c
N = int(input())
mod = 10**9 + 7

# 数列全体の数
A_all = pow(10, N, mod)
# 0を含まない数列の数
A_0 = pow(9, N, mod)
# 9を含まない数列の数
A_9 = pow(9, N, mod)
# 0も9も含まない数列の数
A_0_9 = pow(8, N, mod)

ans = A_all - (A_0 + A_9 - A_0_9)
print(ans % mod)
