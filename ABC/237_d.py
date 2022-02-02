# https://atcoder.jp/contests/abc237/tasks/abc237_d

from collections import deque

dq = deque()

N = int(input())
S = input()

dq.append(N)

# N-1 から 0 まで逆順に
for i in range(N-1, -1, -1):
  if S[i] == 'L':
    dq.append(i)
  else:
    dq.appendleft(i)

print(*dq)