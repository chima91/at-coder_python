MOD = 10**9 + 7

N = int(input())

fact = [1] * 110000
invfact = [1] * 110000

for i in range(1, 110000):
    fact[i] = fact[i - 1] * i % MOD

invfact[110000 - 1] = pow(fact[110000 - 1], MOD - 2, MOD)

for i in range(110000 - 1, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD


def nCk(n, k):
    if k < 0 or n - k < 0:
        return 0
    return fact[n] * invfact[n - k] % MOD * invfact[k] % MOD


for k in range(1, N + 1):
    ans = 0
    for i in range(1, N + 1):
        n = N - (k - 1) * (i - 1)
        if n < i:
            break
        ans += nCk(n, i)
        ans %= MOD
    print(ans)
