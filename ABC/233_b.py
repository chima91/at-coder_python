L, R = map(int, input().split())
S = input()

reversedStr = "".join(list(reversed(S[L-1:R])))
print(S[:L-1] + reversedStr + S[R:])
