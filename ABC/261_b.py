# N = int(input())

# result = []
# for _ in range(N):
#   result.append(list(input()))

# for i in range(N):
#   for j in range(N):
#     if result[i][j] == 'W' and not result[j][i] == 'L':
#       print('incorrect')
#       exit()
#     elif result[i][j] == 'L' and not result[j][i] == 'W':
#       print('incorrect')
#       exit()
#     elif result[i][j] == 'D' and not result[j][i] == 'D':
#       print('incorrect')
#       exit()

# print('correct')


N = int(input())
A = [input() for _ in range(N)]

def is_correct(a, b):
  return a+b in ['WL', 'LW', 'DD']

for i in range(N):
  for j in range(N):
    if i >= j: continue
    if not is_correct(A[i][j], A[j][i]):
      print('incorrect')
      exit()

print('correct')