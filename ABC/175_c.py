# https://atcoder.jp/contests/abc175/tasks/abc175_c

X, K, D = map(int, input().split())

X = abs(X)

if X-K*D > 0:
    print(X-K*D)
else:
    move_count = K-X//D
    plus_pos = X - D*(X//D)
    minus_pos = abs(plus_pos - D)
    if move_count % 2 == 0:
        print(plus_pos)
    else:
        print(minus_pos)
