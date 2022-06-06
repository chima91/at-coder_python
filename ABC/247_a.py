S = list(input())

for i in range(len(S)-1, 0, -1):
  S[i] = S[i-1]
S[0] = '0'

print("".join(S))