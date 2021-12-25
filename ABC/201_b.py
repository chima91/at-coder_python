# https://atcoder.jp/contests/abc201/tasks/abc201_b
N = int(input())
mountains = []
for _ in range(N):
    name, height = map(str, input().split())
    mountains.append([int(height), name])

mountains.sort(reverse=True)
print(mountains[1][1])
