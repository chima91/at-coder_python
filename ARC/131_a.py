A = input()
B = input()

min_a_b = min(int(A), int(B))
max_a_b = max(int(A), int(B))
for x in range(min_a_b, 3*max_a_b):
    if (A in str(x)) & (B in str(2*x)):
        print(x)
        break
