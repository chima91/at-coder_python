N = int(input())

names= {}

for _ in range(N):
  S = input()
  if S not in names:
    print(S)
    names[S] = 1
  else:
    print(f"{S}({names[S]})")
    names[S] += 1

