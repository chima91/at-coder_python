A, B = map(int, input().split())

ans = 0
flag1 = False
flag2 = False
flag4 = False
if A == 1 or B == 1:
    flag1 = True
if A == 2 or B == 2:
    flag2 = True
if A == 3 or B == 3:
    flag1 = True
    flag2 = True
if A == 4 or B == 4:
    flag4 = True
if A == 5 or B == 5:
    flag1 = True
    flag4 = True
if A == 6 or B == 6:
    flag2 = True
    flag4 = True
if A == 7 or B == 7:
    flag1 = True
    flag2 = True
    flag4 = True

if flag1:
    ans += 1
if flag2:
    ans += 2
if flag4:
    ans += 4
print(ans)


# 別解
# A, B = map(int, input().split())
# print(A | B)
