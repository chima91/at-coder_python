import statistics

a, b, c = map(int, input().split())
num_list = [a, b, c]

if statistics.median(num_list) == b:
  print("Yes")
else:
  print("No")