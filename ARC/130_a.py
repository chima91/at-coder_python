n = int(input())
s = input()

ans = []
for i in range(n-1):
    print("i:", i)
    for j in range(i+1, n):
        print("j:", j)
        if(s[0:i]+s[i+1:n] == s[0:j]+s[j+1:n]):
            ans.append(1)
print(len(ans))
