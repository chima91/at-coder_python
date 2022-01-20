# https://atcoder.jp/contests/abc149/tasks/abc149_d
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

my_hands = []
ans = 0

for i in range(N):
    if T[i] == "r":
        if i < K:
            ans += P
            my_hands.append("p")
        elif i >= K and my_hands[i-K] != "p":
            ans += P
            my_hands.append("p")
        else:
            my_hands.append("x")
    if T[i] == "s":
        if i < K:
            ans += R
            my_hands.append("r")
        elif i >= K and my_hands[i-K] != "r":
            ans += R
            my_hands.append("r")
        else:
            my_hands.append("x")
    if T[i] == "p":
        if i < K:
            ans += S
            my_hands.append("s")
        elif i >= K and my_hands[i-K] != "s":
            ans += S
            my_hands.append("s")
        else:
            my_hands.append("x")

print(ans)
