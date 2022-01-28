# Big O Notation

# O(log(n))
def func1(n):
    if n <= 1:
        return
    else:
        print(n)
        func1(n/2)


# O(n)
def func2(numbers):
    for num in numbers:
        print(num)


# O(n * log(n))
def func3(n):
    for i in range(int(n)):
        print(i, end=' ')
    print()

    if n <= 1:
        return
    func3(n/2)


# 0(n ** 2)
def func4(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i], numbers[j])
        print()
