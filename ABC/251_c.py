N = int(input())
S, T = [], []

for i in range(N):
  s,t = input().split()
  S.append(s)
  T.append(int(t))

best = -1
best_score = -1

appeared = set()
for i in range(N):
  if S[i] in appeared:
    continue
  appeared.add(S[i])
  if best_score < T[i]:
    best = i
    best_score = T[i]

print(best + 1)