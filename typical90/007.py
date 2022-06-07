from bisect import bisect_left

N = int(input())
A = list(map(int, input().split())) + [-10**18, +10**18]
A.sort()
Q = int(input())

for _ in range(Q):
  B = int(input())
  idx = bisect_left(A, B)
  nxt = A[idx]
  prev = A[idx-1]
  print(min(nxt-B, B-prev))

