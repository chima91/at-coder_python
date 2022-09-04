n, m = map(int, input().split())
a = [*(map(int, input().split()))]

s, t = sum([a[i] * (i + 1) for i in range(m)]), sum(a[:m])
c = s

for i in range(n - m):
    s -= t - a[i + m] * m
    t -= a[i] - a[i + m]
    c = max(c, s)
print(c)
