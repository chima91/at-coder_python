N = int(input())

class1_sum = [0] * (N+1)
class2_sum = [0] * (N+1)

for i in range(N):
  class1_sum[i+1] = class1_sum[i]
  class2_sum[i+1] = class2_sum[i]
  C, P = map(int, input().split())
  if C == 1:
    class1_sum[i+1] += P
  else:
    class2_sum[i+1] += P

Q = int(input())

for _ in range(Q):
  L, R = map(int, input().split())
  L -= 1
  R -= 1
  print(class1_sum[R+1] - class1_sum[L], class2_sum[R+1] - class2_sum[L])
