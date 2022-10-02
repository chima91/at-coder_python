N = int(input())

ans = format(N, 'x').upper()
if len(ans) == 1:
    ans = f"0{ans}"
print(ans)
