A, B = map(int, input().split())

if A == B:
    print("1.000")
    exit()
if B == 0:
    print("0.000")
    exit()
ans = (B * 10**3 * 2 + A) // (A*2)
print("0.{}".format(ans))
