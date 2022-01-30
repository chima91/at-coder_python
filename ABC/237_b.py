import numpy as np

H, W = map(int, input().split())

matrix = []
for _ in range(H):
  matrix.append(list(map(int, input().split())))

ans = np.transpose(matrix)
for w in range(W):
    print(*ans[w])