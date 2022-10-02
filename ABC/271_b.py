N, Q = map(int, input().split())

nums = []
for _ in range(N):
    nums.append(list(map(int, input().split())))

for _ in range(Q):
    s, t = map(int, input().split())
    print(nums[s-1][t])
