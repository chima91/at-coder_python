# https://atcoder.jp/contests/typical90/tasks/typical90_b

from itertools import combinations

N = int(input())

if N % 2 == 1:
  exit()

def to_parentheses(opens):
  chars = [')'] * N
  for open_pos in opens:
    chars[open_pos] = '('
  return ''.join(chars)

for opens in combinations(list(range(N)), N//2):
  parentheses = to_parentheses(opens)
  cnt = 0
  ok = True
  for c in parentheses:
    if c == '(':
      cnt += 1
    else:
      cnt -= 1
    if cnt < 0:
      ok = False

  if ok:
    print(parentheses)