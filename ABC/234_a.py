def weird(x):
    return x**2 + 2*x + 3


t = int(input())

print(weird(weird(weird(t) + t) + weird(weird(t))))
