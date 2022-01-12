# https://atcoder.jp/contests/abc189/tasks/abc189_c

# テストケース作成
# path = "./test.txt"
# s = "1"
# for i in range(10**4 - 1):
#     s += " 1"
# with open(path, mode='w') as f:
#     f.write(s)

N = int(input())
A = list(map(int, input().split()))

ans = -10**15
for l in range(N):
    A_min = A[l]
    for r in range(l, N):
        A_min = min(A_min, A[r])
        ans = max(ans, A_min * (r-l+1))

print(ans)
