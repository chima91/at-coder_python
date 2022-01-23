# https://atcoder.jp/contests/abc174/tasks/abc174_c

K = int(input())

remainder = 0
for i in range(1, K+1):
    remainder = remainder*10 + 7
    if remainder % K == 0:
        print(i)
        exit()
    remainder %= K

print(-1)
