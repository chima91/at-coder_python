N, X = map(int, input().split())

ans = []

for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    for _ in range(N):
        ans.append(char)

print(ans[X-1])
