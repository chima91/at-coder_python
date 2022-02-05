# https://atcoder.jp/contests/abc182/tasks/abc182_c

N = int(input())

amari1 = False
amari2 = False
amari_all = N % 3

N = str(N)
for i in range(len(N)):
    keta_num = int(N[i])
    if keta_num % 3 == 1:
        amari1 = True
    elif keta_num % 3 == 2:
        amari2 = True

# Nを3で割った余りが0の場合 → 1つも桁を消さなくて良い。
if amari_all == 0:
    print(0)
# Nを3で割った余りが1の場合 → 余りが1の桁が存在するかしないかで場合分け
elif amari_all == 1:
    # 余りが1の桁が存在する場合
    if amari1 == True:
        if len(N) <= 1:
            print(-1)
        else:
            print(1)
    # 余りが1の桁が存在しない場合
    else:
        if len(N) <= 2:
            print(-1)
        else:
            print(2)
# Nを3で割った余りが2の場合 → 余りが2の桁が存在するかしないかで場合分け
elif amari_all == 2:
    # 余りが2の桁が存在する場合
    if amari2 == True:
        if len(N) <= 1:
            print(-1)
        else:
            print(1)
    # 余りが2の桁が存在しない場合
    else:
        if len(N) <= 2:
            print(-1)
        else:
            print(2)
