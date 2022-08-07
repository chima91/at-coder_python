N, M = map(int, input().split())
edge = [[False] * N for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u][v] = True
    edge[v][u] = True

ans = 0
for a in range(N):
    for b in range(a + 1, N):
        for c in range(b + 1, N):
            if edge[a][b] == True and edge[b][c] == True and edge[c][a] == True:
                ans += 1

print(ans)
