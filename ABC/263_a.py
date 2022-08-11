# A, B, C, D, E = map(int, input().split())

# l = [A, B, C, D, E]

# import collections

# c = collections.Counter(l)

# ans = "Yes"
# for cnt in c.values():
#     if cnt not in [2, 3]:
#         print("No")
#         exit()

# print(ans)


# 別解

cnt = [0] * 14

cards = list(map(int, input().split()))

for card in cards:
    cnt[card] += 1

check = []
for c in cnt:
    if c != 0:
        check.append(c)

if check == [2, 3] or check == [3, 2]:
    print("Yes")
else:
    print("No")
