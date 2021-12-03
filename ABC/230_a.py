N = int(input())
if N >= 42:
    print("AGC" + "0" + str(N+1))
elif N <= 9:
    print("AGC" + "00" + str(N))
else:
    print("AGC" + "0" + str(N))
