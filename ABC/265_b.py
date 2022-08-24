N, M, T = map(int, input().split())
A = list(map(int, input().split()))

bonus = [0] * N
for _ in range(M):
    x, y = map(int, input().split())
    bonus[x - 1] = y

for i in range(1, N):
    T -= A[i - 1]
    if T <= 0:
        print("No")
        exit()
    T += bonus[i]
    # print(T)

print("Yes")

# print(bonus)

# bonux_T_sum = 0
# for i in range(M):
#     x, y = map(int, input().split())
#     bonux_T_sum += y

# if T + bonux_T_sum <= sum(A):
#     print("No")
# else:
#     print("Yes")
