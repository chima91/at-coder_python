import bisect

q=int(input())
s=[]

for _ in range(q):
  q=list(map(int,input().split()))

  if q[0]==1:
    bisect.insort(s,q[1])

  if q[0]==2:
    r=bisect.bisect_right(s,q[1])
    l=bisect.bisect_left(s,q[1])
    if (r-l)!=0:
      del s[l:l+min((r-l),q[2])]

  if q[0]==3:
    print(s[-1]-s[0])