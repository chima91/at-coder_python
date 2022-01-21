# https://atcoder.jp/contests/abc168/tasks/abc168_d

from collections import deque

N, M = map(int, input().split())
# どの部屋からどの部屋に行くことができるか
connect = [[] for i in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    connect[A].append(B)
    connect[B].append(A)

# 訪問済みかどうかのリスト
visited = [False]*(N+1)
visited[1] = True

que = deque()
# キューにはスタート地点の部屋①を入れておく。
que.append(1)

ans = [0] * (N+1)

# 探索開始
while len(que) > 0:
    now_room = que.popleft()
    for to_room in connect[now_room]:
        if visited[to_room] == False:
            visited[to_room] = True
            ans[to_room] = now_room
            que.append(to_room)

print("Yes")
for i in range(2, N+1):
    print(ans[i])
