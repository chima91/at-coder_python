X, K = map(int, input().split())

for i in range(K):
    i10 = 10 ** i
    X = (X + i10 * 5) // (i10 * 10) * (i10 * 10)

print(X)
