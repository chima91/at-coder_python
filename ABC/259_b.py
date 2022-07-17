import math

a, b, d = map(int, input().split())

d = math.radians(d)

a_ = math.cos(d) * a - math.sin(d) * b
b_ = math.sin(d) * a + math.cos(d) * b

print(a_, b_)