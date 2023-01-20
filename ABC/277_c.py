from collections import defaultdict

# n > 1000 あたりで再帰回数がPythonの上限を超え，ランタイムエラーを引き起こす．
import sys
sys.setrecursionlimit(10**6)

# 組み込みの辞書だと存在しないキーはエラーとなる．
edge = defaultdict(list)
N = int(input())

for _ in range(N):
    A, B = map(int, input().split())
    edge[A].append(B)
    edge[B].append(A)

ans = 1

come = set()


def dfs(now):
    come.add(now)
    global ans  # 関数内でグローバル変数に値を代入
    ans = max(ans, now)
    for to in edge[now]:
        if to in come:
            continue
        dfs(to)


dfs(1)

print(ans)
