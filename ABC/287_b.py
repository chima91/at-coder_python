N, M = map(int, input().split())

# S = []
# T = []

# for _ in range(N):
#     S.append(input()[3:])
# for _ in range(M):
#     T.append(input())

S = [input()[-3:] for _ in range(N)]
T = [input() for _ in range(M)]

cnt = 0
for s in S:
    if s in T:
        cnt += 1

print(cnt)
