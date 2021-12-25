X, Y = map(int, input().split())
count = 0
while X < Y:
    count += 1
    X += 10
    if X >= Y:
        print(count)
        exit()

print(0)
