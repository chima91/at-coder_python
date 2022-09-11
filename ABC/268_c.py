N = int(input())
P = list(map(int, input().split()))

ans = [0 for _ in range(N)]

for i in range(N):
    p = P[i] - i
    for j in range(3):
        ans[(p-j+1) % N] += 1

print(max(ans))
