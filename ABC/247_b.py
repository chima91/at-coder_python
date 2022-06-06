N = int(input())
s, t = [], []
for _ in range(N):
  s_, t_ = input().split()
  s.append(s_)
  t.append(t_)

for i in range(N):
  can_give_a_nickname = False
  for S in [s[i], t[i]]:
    # print(f"S:{S}")
    s_ok = True
    for j in range(N):
      if i != j:
        if S == s[j] or S == t[j]:
          s_ok = False
    if s_ok == True:
      can_give_a_nickname = True
  if can_give_a_nickname == False:
    print("No")
    exit()

print("Yes")