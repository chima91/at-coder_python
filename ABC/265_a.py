X, Y, N = map(int, input().split())

ans = 0
if Y / 3 < X:
    ans = Y * (N // 3) + X * (N % 3)
else:
    ans = X * N

print(ans)
