N = int(input())
A = list(map(int, input().split()))

depth = [0, 0]

for i in range(N):
    a = A[i]
    depth.append(depth[a]+1)
    depth.append(depth[a]+1)

for i in range(1, 2*N+2):
    print(depth[i])
