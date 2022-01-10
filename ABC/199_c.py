# https://atcoder.jp/contests/abc199/tasks/abc199_c

N = int(input())
S = input()
Q = int(input())

# 0インデックスを回避
S = "0"+S

# このままだとA文字目とB文字目を入れ替える操作が面倒なため、リスト化
S = list(S)

# 状態を管理する変数
flip = False

for i in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        if flip == False:
            S[A], S[B] = S[B], S[A]
        else:
            if A <= N:
                A += N
            else:
                A -= N
            if B <= N:
                B += N
            else:
                B -= N
            S[A], S[B] = S[B], S[A]
    else:
        flip = not flip

S_left = S[1:N+1]
S_right = S[N+1:]

if flip == True:
    ans = S_right + S_left
else:
    ans = S_left + S_right

print("".join(ans))
