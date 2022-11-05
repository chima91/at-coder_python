N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for q in range(Q):
    query = L[q]
    if A[query-1] == N:
        continue
    if A[query-1]+1 in A:
        continue
    A[query-1] += 1

print(*A)
