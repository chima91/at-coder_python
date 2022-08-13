N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

min_i = 0

for i in range(N):
    if T[i] < T[min_i]:
        min_i = i

ans = [0] * N
now_t = T[min_i]
for i in range(N):
    now_i = (min_i + i) % N
    now_t = min(now_t, T[now_i])
    ans[now_i] = now_t
    now_t += S[now_i]

print(*ans)
