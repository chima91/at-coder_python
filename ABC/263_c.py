N, M = map(int, input().split())

ans = []

for use in range(1 << M):
    tmp = []
    for j in range(M):
        if (use >> j) % 2 == 1:
            tmp.append(j)
    if len(tmp) == N:
        ans.append(tmp)

ans.sort()
for nums in ans:
    for i in range(N):
        nums[i] += 1
    print(*nums)
