N, A, B = map(int, input().split())
S = input()

ans = N * B

for rot in range(N):
    cost = rot * A
    for i in range(N // 2):
        opo = N-1-i
        if S[(i+rot) % N] != S[(rot+opo) % N]:
            cost += B
    ans = min(ans, cost)

print(ans)
