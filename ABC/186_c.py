def judge_ten(x):
    x = str(x)
    if '7' in x:
        return True
    else:
        return False


def judge_eight(x):
    s = ''
    while x > 0:
        s = str(x % 8) + s
        x //= 8
    return True if '7' in s else False


N = int(input())

ans = 0
for i in range(1, N+1):
    if judge_ten(i) == False and judge_eight(i) == False:
        ans += 1

print(ans)
