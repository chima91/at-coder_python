N = int(input())
S = [input() for _ in range(N)]

# x方向(垂直方向)にどれだけ動くか
dxs = [0, 1, 1, 1]
# y方向(水平方向)にどれだけ動くか
dys = [1, 1, 0, -1]

for i in range(N):
  for j in range(N):
    for d in range(4):
      dx = dxs[d]
      dy = dys[d]
      white_cnt = 0
      for k in range(6):
        new_x = i + dx*k
        new_y = j + dy*k
        if not (0 <= new_x < N and 0 <= new_y < N):
          white_cnt = 100
          break
        if S[new_x][new_y] == '.':
          white_cnt += 1
      if white_cnt <= 2:
        print("Yes")
        exit()

print("No")


# 今回はグリッドは使わない

# grid = []
# for i in range(N):
#   S = list(input())
#   grid.append(S)