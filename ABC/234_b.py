import math


def distance(a, b):
    d = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    return d


N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append([x, y])

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        # print([i, j])
        dis = distance(points[i], points[j])
        if dis > ans:
            ans = dis

print(ans)
