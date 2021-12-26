# https://atcoder.jp/contests/abc192/tasks/abc192_c
N, K = map(int, input().split())


def g1(x):
    x = str(x)
    x = list(x)
    x.sort(reverse=True)
    x = ''.join(x)
    return int(x)


def g2(x):
    x = str(x)
    x = list(x)
    x.sort()
    x = ''.join(x)
    return int(x)


def f(x):
    return g1(x) - g2(x)


a = N
for _ in range(int(K)):
    a = f(a)

print(a)
