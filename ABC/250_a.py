# https://atcoder.jp/contests/abc250/tasks/abc250_a

H, W = map(int, input().split())
R, C = map(int, input().split())

def inside(x, y):
  return 1 <= x <= H and 1 <= y <= W

ans = inside(R+1, C) + inside(R-1, C) + inside(R, C+1) + inside(R, C-1)
print(ans)