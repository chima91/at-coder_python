N = int(input())

S_set = []
for _ in range(N):
    S = input()
    S_set.append(S)

    if (S[0] not in ["H", "D", "C", "S"]) or (S[1] not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]):
        print("No")
        exit()

if len(set(S_set)) != N:
    print("No")
    exit()

print("Yes")
