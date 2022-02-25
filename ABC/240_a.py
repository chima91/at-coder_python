# a, b = map(int, input().split())

# if a == 1 and b == 10:
#   print('Yes')
# elif b-a == 1:
#   print('Yes')
# else:
#   print('No')


# 別解
# aとbの差が1か9になるか
a, b = map(int, input().split())

if (a-b) % 10 in [1, 9]:
  print('Yes')
else:
  print('No')