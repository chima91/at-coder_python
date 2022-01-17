# https://atcoder.jp/contests/abc173/tasks/abc173_c
H, W, K = map(int, input().split())
c = []
for row in range(H):
    c.append(list(input()))

ans = 0

# ここからBit全探索
for row_red in range(1 << H):
    for col_red in range(1 << W):
        black = 0
        for row in range(H):
            for col in range(W):
                if row_red >> row & 1 == 0 and col_red >> col & 1 == 0:
                    if c[row][col] == "#":
                        black += 1
        if black == K:
            ans += 1

print(ans)
