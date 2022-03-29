# N = int(input())
# T = input()

# where = 'right'
# ans = [0, 0]
# for i in range(N):
#   if T[i] == 'S':
#     if where == 'right':
#       ans[0] += 1
#     elif where == 'down':
#       ans[1] -= 1
#     elif where == 'left':
#       ans[0] -= 1
#     else:
#       ans[1] += 1
#   else:
#     if where == 'right':
#       where = 'down'
#     elif where == 'down':
#       where = 'left'
#     elif where == 'left':
#       where = 'up'
#     else:
#       where = 'right'

# print(*ans)


# x, yの増減を配列で管理する別解
N = int(input())
T = input()

x, y = 0, 0
d = 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for t in T:
  if t == 'S':
    x += dx[d]
    y += dy[d]
  else:
    d += 1
    d %= 4

print(x, y)
