N, X = map(int, input().split())
A = list(map(int, input().split()))

# Nの数だけFalseの配列を作成
bool_array = [False for _ in range(N)]
# 最初のインデックスはX
idx = X
while True:
    bool_array[idx-1] = True
    idx = A[idx-1]
    if bool_array[idx-1] == True:
        break

print(bool_array.count(True))
