a, b = map(int, input().split())

ans = "Easy"
for _ in range(min(len(str(a)), len(str(b)))):
    if (a % 10)+(b % 10) >= 10:
        ans = "Hard"
        break
    a //= 10
    b //= 10

print(ans)
