# https://atcoder.jp/contests/abc141/tasks/abc141_d

import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))

# heapqは最小値しか取り出せないため、Aの値を全てマイナスにして大小を逆転させる。
A_minus = []
for i in range(N):
    A_minus.append((-1) * A[i])

heapq.heapify(A_minus)

for _ in range(M):
    X = heapq.heappop(A_minus)
    # X //= 2 にするとXがマイナスのため小数点の切り捨てで失敗する
    X /= 2
    X = int(X)
    # 2で割った要素をheapに戻す
    heapq.heappush(A_minus, X)

ans = (-1) * sum(A_minus)
print(ans)
