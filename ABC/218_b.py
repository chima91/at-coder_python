# P = list(map(int, input().split()))

# S = [chr(p - 1 + ord("a")) for p in P]

# print(*S, sep="")

# 別解
P = list(map(int, input().split()))

chars = list(map(lambda x: chr(x - 1 + ord("a")), P))

print("".join(chars))
