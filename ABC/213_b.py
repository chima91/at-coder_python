N = int(input())
A = list(map(int, input().split()))

tuples = [(A[i], i+1) for i in range(N)]
tuples.sort()
print(tuples[-2][1])