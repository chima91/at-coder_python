N, L = map(int, input().split())
K = int(input())
A = [0] + list(map(int, input().split())) + [L]

# 長さl以上でk個以上作れるか(貪欲法)
def ok(l):
  left_idx = 0
  for _ in range(K+1):
    right_idx = left_idx
    while (right_idx < len(A) and
          A[right_idx] - A[left_idx] < l):
      right_idx += 1
    if right_idx == len(A):
      return False
    left_idx = right_idx
  return True

# 二分探索(bottom: OK, top: NG)
bottom, top = 1, L+1
while top - bottom > 1:
  mid = (top + bottom) // 2
  if ok(mid):
    bottom = mid
  else:
    top = mid

print(bottom)