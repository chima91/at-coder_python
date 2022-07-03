K = int(input())

HH = 21
MM = K % 60

if K >= 60:
  HH += 1

if MM < 10:
  MM = "0" + str(MM)

print(f"{HH}:{MM}")