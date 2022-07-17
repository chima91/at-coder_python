S = input()
T = input()

char_s = S[0]
count_s = 1
S_char = []
S_count = []
for i in range(1, len(S)):
  if char_s == S[i]:
    count_s += 1
  else:
    S_char.append(char_s)
    S_count.append(count_s)
    char_s = S[i]
    count_s = 1
S_char.append(char_s)
S_count.append(count_s)

char_t = T[0]
count_t = 1
T_char = []
T_count = []
for i in range(1, len(T)):
    if char_t == T[i]:
        count_t += 1
    else:
        T_char.append(char_t)
        T_count.append(count_t)
        char_t = T[i]
        count_t = 1
T_char.append(char_t)
T_count.append(count_t)

if S_char != T_char:
  print("No")
  exit()
for i in range(len(S_char)):
  if S_count[i] == T_count[i]:
    continue
  elif T_count[i] > S_count[i] >= 2:
    continue
  else:
    print("No")
    exit()
print("Yes")