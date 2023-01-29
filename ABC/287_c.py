import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

# DFS
visited = [False for _ in range(N)]


def dfs(now):
    visited[now] = True
    for vertex in graph[now]:
        if not visited[vertex]:
            dfs(vertex)


dfs(0)
if not all(visited):
    print("No")
    exit()

cnt1 = 0
for i in graph:
    if len(i) == 1:
        cnt1 += 1
    elif len(i) != 2:
        print("No")
        exit()

print("Yes" if cnt1 == 2 else "No")
