S = [input() for _ in range(10)]

INF = 10**18
A, B, C, D = INF, -INF, INF, -INF

for i in range(10):
    for j in range(10):
        if S[i][j] == '#':
            A = min(A, i+1)
            B = max(B, i+1)
            C = min(C, j+1)
            D = max(D, j+1)

print(A, B)
print(C, D)
