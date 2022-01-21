# https://atcoder.jp/contests/abc146/tasks/abc146_c
def price(N):
    N_str = str(N)
    d = len(N_str)
    return A*N + B*d


A, B, X = map(int, input().split())
# 例外(整数1を買えない場合)
if X < price(1):
    print(0)
    exit()

# 二分探索の探索範囲（左端と右端を決める）
left = 1
right = 10**20

# 探索開始。終了条件は左端と右端の差が1になるまで
while 1 < right - left:
    N = (left + right) // 2
    if price(N) <= X:
        left = N
    else:
        right = N

if 10**9 < left:
    left = 10 ** 9
print(left)
