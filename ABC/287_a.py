N = int(input())

for_cnt = 0
against_cnt = 0
for _ in range(N):
    s = input()
    if s == "For":
        for_cnt += 1
    else:
        against_cnt += 1
    if for_cnt > N / 2:
        print("Yes")
        exit()
    elif against_cnt > N / 2:
        print("No")
        exit()
