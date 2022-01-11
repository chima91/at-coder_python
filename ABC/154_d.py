# https://atcoder.jp/contests/abc154/tasks/abc154_d
N, K = map(int, input().split())
p = list(map(int, input().split()))

p_ex = []


# 数列の和の公式を使う
def ex_formula(x):
    return((1/2)*x*(x+1)*(1/x))


# 期待値を計算したリスト
for i in range(N):
    p_ex.append(ex_formula(p[i]))

# 累積和のリスト
# 最初に期待値リストの0番目の値を入れておく
p_ex_cum = [p_ex[0]]
for i in range(1, N):
    p_ex_cum.append(p_ex_cum[i-1] + p_ex[i])

# ダミーを定義
ans = -10**15

for i in range(N-K+1):
    if i == 0:
        ans_tmp = p_ex_cum[i+K-1]
    else:
        ans_tmp = p_ex_cum[i+K-1] - p_ex_cum[i-1]
    ans = max(ans, ans_tmp)

print(ans)
