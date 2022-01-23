# https://atcoder.jp/contests/abc151/tasks/abc151_d

from collections import deque

H, W = map(int, input().split())
maze = []
for i in range(H):
    maze.append(list(input()))


def explore(start_row, start_col):
    maze_count = [[-1] * W for _ in range(H)]
    maze_count[start_row][start_col] = 0

    que = deque()
    que.append([start_row, start_col])

    while len(que) > 0:
        now_row, now_col = que.popleft()
        now_count = maze_count[now_row][now_col]

        # 左
        if 0 <= now_row-1 < H and 0 <= now_col < W:
            if maze[now_row-1][now_col] == ".":
                if maze_count[now_row-1][now_col] == -1:
                    maze_count[now_row-1][now_col] = now_count+1
                    que.append([now_row-1, now_col])
        # 右
        if 0 <= now_row+1 < H and 0 <= now_col < W:
            if maze[now_row+1][now_col] == ".":
                if maze_count[now_row+1][now_col] == -1:
                    maze_count[now_row+1][now_col] = now_count+1
                    que.append([now_row+1, now_col])
        # 上
        if 0 <= now_row < H and 0 <= now_col-1 < W:
            if maze[now_row][now_col-1] == ".":
                if maze_count[now_row][now_col-1] == -1:
                    maze_count[now_row][now_col-1] = now_count+1
                    que.append([now_row, now_col-1])
        # 下
        if 0 <= now_row < H and 0 <= now_col+1 < W:
            if maze[now_row][now_col+1] == ".":
                if maze_count[now_row][now_col+1] == -1:
                    maze_count[now_row][now_col+1] = now_count+1
                    que.append([now_row, now_col+1])

    max_count = 0
    for row in range(H):
        for col in range(W):
            max_count = max(max_count, maze_count[row][col])

    return max_count


ans = 0
for row in range(H):
    for col in range(W):
        if maze[row][col] == ".":
            ans = max(ans, explore(row, col))

print(ans)
