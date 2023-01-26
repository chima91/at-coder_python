N, P, Q, R, S = map(int, input().split())
P -= 1
Q -= 1
R -= 1
S -= 1
A = list(map(int, input().split()))

B = A[:]
B[P:Q+1] = A[R:S+1]
B[R:S+1] = A[P:Q+1]

print(*B)
