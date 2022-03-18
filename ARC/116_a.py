# https://atcoder.jp/contests/arc116/tasks/arc116_a

T = int(input())

for _ in range(T):
  N = int(input())

  # Nが2で2回以上割れるなら
  if N % 2**2 == 0:
    print("Even")
  # Nが2で1回割れるなら
  elif N % 2**1 == 0:
    print("Same")
  # Nが2で0回割れるなら
  else:
    print("Odd")