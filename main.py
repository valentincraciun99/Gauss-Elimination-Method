from numpy import array, zeros, fabs


def elimination(matrix):
    for k in range(n - 2):
        factor = a[k][k]


a = array([[2, 1, 3],
           [3, 2, 7],
           [1, 7, 2]],
          float)
b = array([5, 7, 2], float)
n = len(b)
x = zeros(n, float)


print(a[1, 1])
print(b)

# Elimination
for k in range(n):
    for i in range(k + 1, n):
        if a[i,k] == 0:
            continue
        factor = a[k,k] / a[i,k]
        for j in range(k, n):
            a[i,j] = a[k,j] - a[i,j] * factor
            b[i] = b[k] - factor * b[i]

print(a)
print(b)

# Elimination


