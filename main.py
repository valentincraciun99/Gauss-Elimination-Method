from numpy import array, zeros, fabs,linalg

def elimination(matrix):
    for k in range(n - 2):
        factor = a[k][k]


a = array([[0,7,-1,1,1],
           [0,3,4,1,7],
           [6,2,0,2,-1],
           [2,1,2,0,2],
           [3,4,1,-2,1]],
          float)
b = array([5,7,2,3,4], float)
n = len(b)
x = zeros(n, float)
eps = 0.5e-5

print(a[1, 1])
print(b)

# Elimination
for k in range(n):
    if fabs(a[k, k] < eps):
        for i in range(k + 1, n):
            if (fabs(a[i, k] > a[k, k])):
                a[[k, i]] = a[[i, k]]
                b[[k, i]] = b[[i, k]]
                break

    for i in range(k + 1, n):
        if a[i, k] == 0:
            continue
        factor = a[k, k] / a[i, k]
        for j in range(k, n):
            a[i, j] = a[k, j] - a[i, j] * factor
            b[i] = b[k] - factor * b[i]

print(a)
print(b)

# Elimination
