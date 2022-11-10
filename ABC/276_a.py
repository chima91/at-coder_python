S = input()

if 'a' in S:
    ans = S[::-1].find('a')
    print(len(S)-ans)

else:
    print(-1)
