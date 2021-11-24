S, T, X = map(int, input().split())

if S < T:
    print("Yes" if S <= X < T else "No")
else:
    print("Yes" if S <= X or X < T else "No")
