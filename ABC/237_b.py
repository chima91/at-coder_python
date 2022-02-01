# import numpy as np

# H, W = map(int, input().split())

# matrix = []
# for _ in range(H):
#   matrix.append(list(map(int, input().split())))

# ans = np.transpose(matrix)
# for w in range(W):
#     print(*ans[w])


# ↓ numpyを使わない解き方 ↓
H, W = map(int, input().split())
matrix = [
  list(map(int, input().split())) for _ in range(H)
]

for row in zip(*matrix):
  print(*row)