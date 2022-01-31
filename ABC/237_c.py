S = input()

a_cnt = 0
for c in S:
  if c == 'a':
    a_cnt += 1
if a_cnt == len(S):
  print('Yes')
  exit()

left_a = 0
right_a = 0

while S[left_a] == 'a':
  left_a += 1
while S[-(right_a+1)] == 'a':
  right_a += 1

middle = S[left_a:len(S)-right_a]

if middle == middle[::-1] and left_a <= right_a:
  print('Yes')
else:
  print('No')