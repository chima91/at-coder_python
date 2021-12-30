# https://atcoder.jp/contests/abc180/tasks/abc180_c
def divisor_list(N):
    divisor = []
    i = 1
    while i**2 <= N:
        if N % i == 0:
            divisor.append(i)
            if i != N//i:
                divisor.append(N//i)
        i += 1
    divisor.sort()
    return divisor


N = int(input())
ans = divisor_list(N)

for div in ans:
    print(div)
