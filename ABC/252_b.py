N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

maxB = -10 ** 18
for b in B:
  if A[b-1] > maxB:
    maxB = A[b-1]

if max(A) == maxB:
  print("Yes")
else:
  print("No")
