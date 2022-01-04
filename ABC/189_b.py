# https://atcoder.jp/contests/abc189/tasks/abc189_b
N, X = map(int, input().split())

ans = -1
sum = 0
for i in range(1, N+1):
    V, P = map(int, input().split())
    sum += V * P
    if sum > X * 100:
        ans = i
        break

print(ans)
