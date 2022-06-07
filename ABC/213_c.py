from bisect import bisect_left

H, W, N = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(N)]

anum = list(set(x for x, _ in cards))
bnum = list(set(y for _, y in cards))

anum.sort()
bnum.sort()

for a,b in cards:
  ca = bisect_left(anum, a)
  cb = bisect_left(bnum, b)
  print(ca+1, cb+1)