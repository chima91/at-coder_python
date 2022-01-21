# https://atcoder.jp/contests/abc197/tasks/abc197_c

N = int(input())
A = list(map(int, input().split()))


def calc_or(left, right):
    result = 0
    for i in range(left, right):
        result = result | A[i]
    return result


# 答えの初期値は十分大きい数
ans = 2 ** 40

# ここからBit全探索
for i in range(1 << (N+1)):
    if i & 1 == 0 or i >> N & 1 == 0:
        continue
    partitions = []
    for shift in range(N+1):
        if i >> shift & 1 == 1:
            partitions.append(shift)
    ans_tmp = 0
    for j in range(len(partitions)-1):
        ans_tmp = ans_tmp ^ calc_or(partitions[j], partitions[j+1])
    ans = min(ans, ans_tmp)

print(ans)
