N = int(input())
A = [-1] + list(map(int, input().split()))

solo = 0
pair = 0

for i in range(1, N + 1):
    if A[i] == i:
        solo += 1
        continue
    if A[A[i]] == i:
        pair += 1

pair //= 2

print(pair + (solo * (solo - 1) // 2))
