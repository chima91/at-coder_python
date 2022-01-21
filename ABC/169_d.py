# https://atcoder.jp/contests/abc169/tasks/abc169_d

def prime_factorize(N):
    if N == 1:
        return [1]
    prime_list = []
    i = 2
    while i**2 <= N:
        if N % i == 0:
            prime_list.append(i)
            N //= i
        else:
            i += 1
    # ループが終了した際、Nが1でなければそれも素因数としてリストに追加
    if N != 1:
        prime_list.append(N)
    return prime_list


N = int(input())
# もしN=1なら例外として、0を出力して終わり。
if N == 1:
    print(0)
    exit()

# Nの素因数分解
prime_N = prime_factorize(N)
# Nの素因数の種類を確認
prime_N = set(prime_N)

# 操作回数 = 答え
ans = 0

# 素因数^1, 素因数^2, ..., で割り算していく
for pr in prime_N:
    # 割り切れなかったらbreakするからexの探索範囲は大きければ何でも良い。
    for ex in range(1, 10**10):
        if N % (pr ** ex) == 0:
            ans += 1
            N //= pr ** ex
        else:
            # 割り切れなかった場合、次の素数(pr)へ
            break

print(ans)
