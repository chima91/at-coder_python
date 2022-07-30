N = int(input())
A, B, C = map(int, input().split())

ans = 10000

for i in range(10000):
    for j in range(10000):
        rest = N - A * i - B * j
        if rest < 0:
            break
        if rest % C == 0:
            ans = min(ans, i + j + rest // C)

print(ans)
