s00, s01 = list(input())
s10, s11 = list(input())

if (s00+s01+s10+s11).count('#') >= 3:
    print("Yes")
else:
    if ((s00+s11).count('#') == 2) or ((s10+s01).count('#') == 2):
        print("No")
    else:
        print("Yes")
