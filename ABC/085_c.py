# https://atcoder.jp/contests/abc085/tasks/abc085_c
n, y = map(int, input().split())

for xx in range(n+1):
    for yy in range(n-xx+1):
        if (xx*10000 + yy*5000 + (n-xx-yy)*1000) == y:
            print(xx, yy, n-xx-yy)
            exit()

print('-1 -1 -1')
