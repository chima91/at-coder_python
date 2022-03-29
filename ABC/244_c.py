N = int(input())

# 高橋君か青木君によって既に宣言された整数を管理
used = [False] * (2*N+2)

for _ in range(N+1):
  takahashiNum = 1
  while used[takahashiNum]:
    takahashiNum += 1
  # 高橋君が整数を宣言
  print(takahashiNum)
  # 高橋君が宣言した整数を宣言済みにする
  used[takahashiNum] = True
  # 青木君が整数を宣言
  aokiNum = int(input())
  # 青木君が宣言した整数を宣言済みにする
  used[aokiNum] = True
