N, B, K = map(int, input().split())
c = list(map(int, input().split()))

MOD = (10 ** 9) + 7

def twice(dp, n):
  twice_dp = [0] * B
  pow10n = pow(10, n, B)
  for upper_mod in range(B):
    for lower_mod in range(B):
      twice_dp[(upper_mod * pow10n + lower_mod) % B] += dp[upper_mod] * dp[lower_mod] % MOD
      twice_dp[(upper_mod * pow10n + lower_mod) % B] %= MOD
  return twice_dp

def add1(dp):
  next_dp = [0] * B
  for i in range(B):
    for d in c:
      next_dp[(i * 10 + d) % B] += dp[i]
      next_dp[(i * 10 + d) % B] %= MOD
  return next_dp

def calc(n):
  if n == 0:
    res = [0] * B
    res[0] = 1
    return res
  if n % 2 == 1:
    return add1(calc(n-1))
  else:
    return twice(calc(n//2), n//2)

print(calc(N)[0])