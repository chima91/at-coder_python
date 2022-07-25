L1, R1, L2, R2 = map(int, input().split())

field = [0] * 1000

for i in range(L1, R1):
  field[i] += 1
for i in range(L2, R2):
  field[i] += 1

ans = 0
for cnt in field:
  if cnt == 2:
    ans +=1

print(ans)