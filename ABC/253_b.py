H, W = map(int, input().split())

S = []
for _ in range(H):
  S += [input()]

positions = []
for i in range(H):
  for j in range(W):
    if S[i][j] == 'o':
      positions.append((i, j))

x1, y1 = positions[0]
x2, y2 = positions[1]
print(abs(x1-x2) + abs(y1-y2))