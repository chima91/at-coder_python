N = int(input())

now = 0
cut = [now]

A = list(map(int, input().split()))
for a in A:
  now += a
  now %= 360
  cut.append(now)

cut.sort()

ans = 0
for i in range(N-1):
  ans = max(ans, cut[i+1]-cut[i])

ans = max(ans, 360-cut[-1])

print(ans)