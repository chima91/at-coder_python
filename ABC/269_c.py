from itertools import product

N = int(input())
n = format(N, "b")

lis = [[] for _ in range(len(n))]
for i in range(len(n)):
    if n[i] == "0":
        lis[i] = ["0"]
    else:
        lis[i] = ["0", "1"]

lst = [*map(list, product(*lis))]
for i in lst:
    i = int("".join(i), 2)
    print(i)
