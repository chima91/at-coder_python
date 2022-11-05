N = int(input())
S = list(input())
W = list(map(int, input().split()))

people = []
cnt = 0

for i in range(N):
    people.append((W[i], S[i]))
    if S[i] == '1':
        cnt += 1

ans = cnt
people.sort()

for i in range(N):
    w, s = people[i]
    if s == '0':
        cnt += 1
    if s == '1':
        cnt -= 1
    if i+1 == N or people[i+1][0] != w:
        ans = max(ans, cnt)

print(ans)
