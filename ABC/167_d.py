# https://atcoder.jp/contests/abc167/tasks/abc167_d
N, K = map(int, input().split())
# Aは1indexで受け取る
A = [0] + list(map(int, input().split()))

# ループの始まりはいくつか、ループの周期はいくつか
visited = [-1] * (N+1)
visited[1] = 0

now_town = 1
move_cnt = 0

# ここからシミュレーション（探索範囲は十分大きければ何でも良い）
for _ in range(10**6):
    move_cnt += 1
    now_town = A[now_town]
    if move_cnt == K:
        print(now_town)
        exit()
    if visited[now_town] == -1:
        visited[now_town] = move_cnt
    # 以前訪れた時の移動回数からループの周期を計算
    else:
        cycle = move_cnt - visited[now_town]
        break

K -= move_cnt
K %= cycle
for _ in range(K):
    now_town = A[now_town]

print(now_town)
