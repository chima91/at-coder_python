X, Y, Z = map(int, input().split())

ans = 0
if X > 0:
    if X > Y > 0:
        if Z > Y:
            ans = -1
        else:
            if Z > 0:
                ans = X
            else:
                ans = 2 * abs(Z) + X
    else:
        ans = X
else:
    if X < Y < 0:
        if Z < Y:
            ans = -1
        else:
            if Z > 0:
                ans = 2 * Z + abs(X)
            else:
                ans = abs(X)
    else:
        ans = abs(X)

print(ans)
