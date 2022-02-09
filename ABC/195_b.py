A, B, W = map(int, input().split())

# gをkgに変換
W_g = W*1000

# 答えの最小値(初期値は大きい数)
min_ans = 10**15
# 答えの最大値(初期値は小さい数)
max_ans = -10**15

# 条件を満たしうる最大の個数はみかん1個当たりの重さが最小かつ最大、つまりB=1かつW=1000の時。
for X in range(1, 10**6+10):
    if A*X <= W_g <= B*X:
        min_ans = min(min_ans, X)
        max_ans = max(max_ans, X)

# 一度も最小値が更新されていなければ、該当するXがなかったということ。
if min_ans == 10**15:
    print("UNSATISFIABLE")
else:
    print(min_ans, max_ans)
