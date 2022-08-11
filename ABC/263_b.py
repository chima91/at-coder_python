N = int(input())
P = [-1, -1] + list(map(int, input().split()))

now = N
cnt = 0

while now != 1:
    cnt += 1
    now = P[now]

print(cnt)
