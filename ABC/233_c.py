N, X = map(int, input().split())
baggages = []

l_prod = 1
for _ in range(N):
  tmp = list(map(int, input().split()))
  l, a = tmp[0], tmp[1:]
  baggages.append(a)
  l_prod *= l

ans = 0
for i in range(l_prod):
  idx = i
  prod = 1
  for bag in baggages:
    prod *= bag[idx % len(bag)]
    idx //= len(bag)
    if prod > X:
      break
  if prod == X:
    ans += 1

print(ans)
