s = []
abc = input()
for i in range(3):
    s.append(abc[i])

bca = s[1]+s[2]+s[0]
cab = s[2]+s[0]+s[1]

print(int(abc)+int(bca)+int(cab))
