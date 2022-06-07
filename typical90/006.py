N, K = map(int, input().split())
S = input()

nxt = [[N+10] * 26 for _ in range(N+1)]

for i in range(N-1, -1, -1):
  for j in range(26):
    nxt[i][j] = nxt[i+1][j]
  nxt[i][ord(S[i]) - ord('a')] = i

ans = ""

now = 0
for l in range(K):
  for c in range(26):
    if nxt[now][c] <= N - (K - l):
      ans += chr(ord('a') + c)
      now = nxt[now][c] + 1
      break

print(ans)