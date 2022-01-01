# https://atcoder.jp/contests/abc203/tasks/abc203_c
N, K = map(int, input().split())

friends = []
for _ in range(N):
    num, money = map(int, input().split())
    friends.append([num, money])
friends.sort()

now_village = 0
now_village += K

for i in range(N):
    if now_village >= friends[i][0]:
        now_village += friends[i][1]
    else:
        break

print(now_village)
