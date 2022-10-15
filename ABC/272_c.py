_, a, s = input(), sorted(map(int, input().split())), [[-9e9], [-9e9]]
for i in a:
    s[i % 2].append(i)
print(max([-1]+[sum(i[-2:])for i in s]))
