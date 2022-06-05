N, K = map(int, input().split())

a = list(map(int, input().split()))

groups = [[] for _ in range(K)]
for i in range(N):
  groups[i % K].append(a[i])
for g in groups:
  g.sort()

new_a = [groups[i % K][i // K] for i in range(N)]

if sorted(new_a) == new_a:
  print("Yes")
else:
  print("No")