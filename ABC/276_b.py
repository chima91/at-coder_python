N, M = map(int, input().split())

connection = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    connection[A-1].append(B)
    connection[B-1].append(A)

for n in range(N):
    connection[n].sort()
    ans = (len(connection[n]), *connection[n])
    print(*ans)
