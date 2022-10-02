N = int(input())
A = list(map(int, input().split()))


def ok(x):
    less_than_x = [e for e in A if e <= x]
    remain = len(set(less_than_x))
    need = x - remain
    extra = N - remain
    return extra // 2 >= need


bottom = 0
top = 3 * 10**5 + 1

while top - bottom > 1:
    middle = (top+bottom) // 2
    if (ok(middle)):
        bottom = middle
    else:
        top = middle
print(bottom)
