N, K, A = map(int, input().split())
ans = 0
if A + (K % N - 1) > N:
    ans = A + (K % N - 1) - N
else:
    ans = A + K % N - 1
    if ans == 0:
        ans = 1
print(ans)
