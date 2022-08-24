H, W = map(int, input().split())
G = [input() for _ in range(H)]

visited = [[False] * W for _ in range(H)]
nowx, nowy = 0, 0

while True:
    visited[nowx][nowy] = True
    char = G[nowx][nowy]
    nxtx, nxty = nowx, nowy
    if char == "U":
        nxtx -= 1
    if char == "D":
        nxtx += 1
    if char == "L":
        nxty -= 1
    if char == "R":
        nxty += 1
    if nxtx < 0 or nxtx >= H or nxty < 0 or nxty >= W:
        print(nowx + 1, nowy + 1)
        exit()
    nowx, nowy = nxtx, nxty
    if visited[nowx][nowy]:
        print(-1)
        exit()
