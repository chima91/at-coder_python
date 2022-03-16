# https://atcoder.jp/contests/abc243/tasks/abc243_b

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt1 = 0
cnt2 = 0
for i in range(len(A)):
  # 含まれている かつ 同じインデックス
  if A[i] == B[i]:
    cnt1 += 1
  # 含まれている が 異なるインデックス
  if A[i] in B:
    cnt2 += 1

print(cnt1, cnt2 - cnt1, sep='\n')