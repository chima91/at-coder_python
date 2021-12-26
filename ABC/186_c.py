N = int(input())

for i in range(1, N+1):
    if ('7' in str(i)) or ('7' in oct(i)):
        N -= 1

print(N)
