n, m = map(int, input().split())
mark = []
for _ in range(n):
    mark.append([0]*n)
for _ in range(m):
    a = list(map(int, input().split()))
    for i in range(1, a[0]+1):
        for j in range(1, a[0]+1):
            mark[a[i]-1][a[j]-1] = 1

for x in mark:
    if 0 in x:
        print("No")
        exit()

print("Yes")
