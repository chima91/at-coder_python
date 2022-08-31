# import numpy as np

# Ax, Ay = map(int, input().split())
# Bx, By = map(int, input().split())
# Cx, Cy = map(int, input().split())
# Dx, Dy = map(int, input().split())

# A = np.array([Ax, Ay])
# B = np.array([Bx, By])
# C = np.array([Cx, Cy])
# D = np.array([Dx, Dy])


# def getX(a, b, c):
#     vec_a = a - b
#     vec_c = c - b

#     length_vec_a = np.linalg.norm(vec_a)
#     length_vec_c = np.linalg.norm(vec_c)
#     inner_product = np.inner(vec_a, vec_c)
#     cos = inner_product / (length_vec_a * length_vec_c)

#     rad = np.arccos(cos)

#     degree = np.rad2deg(rad)

#     return degree


# if (
#     getX(A, B, C) + getX(B, C, D) + getX(C, D, A) < 180
#     or getX(B, C, D) + getX(C, D, A) + getX(D, A, B) < 180
#     or getX(C, D, A) + getX(D, A, B) + getX(A, B, C) < 180
#     or getX(D, A, B) + getX(A, B, C) + getX(B, C, D) < 180
# ):
#     print("No")
# else:
#     print("Yes")


# 別解
def ccw(p1, p2, p3):
    p1[0] -= p2[0]
    p3[0] -= p2[0]
    p1[1] -= p2[1]
    p3[1] -= p2[1]

    return p1[0] * p3[1] - p1[1] * p3[0] < 0


P = []
for i in range(4):
    P.append(list(map(int, input().split())))

for i in range(4):
    if not ccw(P[i][:], P[(i + 1) % 4][:], P[(i + 2) % 4][:]):
        print("No")
        exit()

print("Yes")
