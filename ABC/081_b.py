# https://atcoder.jp/contests/abc081/tasks/abc081_b
import math
N = input()
Alist = list(map(int, input().split()))
ans = float("inf")
for i in Alist:
    ans = min(ans, len(bin(i)) - bin(i).rfind("1") - 1)
print(round(ans))
