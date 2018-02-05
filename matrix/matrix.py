# Copyright (C) 2018 by Joon Jung
#
# This code is licensed under the MIT license (MIT) (http://opensource.org/licenses/MIT)
#

# Strassen Multiplication

# M1 = (A11 + A22)(B11 + B22)
# M2 = (A21 + A22)B11
# M3 = A11(B12 - B22)
# M4 = A22(B21 - B11)
# M5 = (A11 + A12)B22
# M6 = (A21 - A11)(B11 + B12)
# M7 = (A12 - A22)(B21 + B22)

# C11 = M1 + M4 - M5 + M7
# C12 = M3 + M5
# C21 = M2 + M4
# C22 = M1 - M2 + M3 + M6

import numpy as np

# INPUT: This implementation only allows square
# even numbered matrix. The user of
# this function is expected to pad or 
# do something similar before feeding 
# the data.
# OUTPUT: Multiplied Matrix

# Big O bound
# Each call of strassen_multiplication is composed of
# 7f(n-1) + constant operations. Therefore the bound is
# O((7 + O(1))^n and n = log(2, N).
# This leads to O(pow(N, log(2, 7)+O(1))) and gives
# roughly O(pow(N, 2.8)) bound.
def strassen_multiplication(a, b, n):

  n1, n2 = a.shape
  if n != n1 or n != n2:
    print("Only square matrices are acceptted. Please pad your matrices.")
    return 0
  elif n%2 != 0:
    print("Only even matrices are acceptted. Please pad your matrices.")
    return 0

  if n == 2:
    m1 = (a[0][0] + a[1][1]) * (b[0][0] + b[1][1])
    m2 = (a[1][0] + a[1][1]) * b[0][0]
    m3 = a[0][0] * (b[0][1] - b[1][1])
    m4 = a[1][1] * (b[1][0] - b[0][0])
    m5 = (a[0][0] + a[0][1]) * b[1][1]
    m6 = (a[1][0] - a[0][0]) * (b[0][0] + b[0][1])
    m7 = (a[0][1] - a[1][1]) * (b[1][0] + b[1][1])

    c11 = m1 + m4 - m5 + m7 
    c12 = m3 + m5 
    c21 = m2 + m4 
    c22 = m1 - m2 + m3 + m6

    a = np.stack((c11, c21), axis=0)
    b = np.stack((c12, c22), axis=0)
    c = np.stack((a, b), axis=1)

    return c
  
  a11 = a[0:n//2, 0:n//2]
  a12 = a[0:n//2, n//2:n]
  a21 = a[n//2:n, 0:n//2]
  a22 = a[n//2:n, n//2:n]
  
  b11 = b[0:n//2, 0:n//2]
  b12 = b[0:n//2, n//2:n]
  b21 = b[n//2:n, 0:n//2]
  b22 = b[n//2:n, n//2:n]
 
  m1 = strassen_multiplication(a11 + a22, b11 + b22, n//2)
  m2 = strassen_multiplication(a21 + a22, b11, n//2)
  m3 = strassen_multiplication(a11, b12 - b22, n//2)
  m4 = strassen_multiplication(a22, b21 - b11, n//2)
  m5 = strassen_multiplication(a11 + a12, b22, n//2)
  m6 = strassen_multiplication(a21 - a11, b11 + b12, n//2)
  m7 = strassen_multiplication(a12 - a22, b21 + b22, n//2)

  c11 = m1 + m4 - m5 + m7 
  c12 = m3 + m5 
  c21 = m2 + m4 
  c22 = m1 - m2 + m3 + m6

  a = np.concatenate((c11, c12), axis=1)
  b = np.concatenate((c21, c22), axis=1)
  c = np.concatenate((a, b), axis=0)
  
  return c

n = 8

a = np.zeros((n, n))
k = 0
for i in range(n):
  for j in range(n):
    a[i, j] = k
    k += 1

b = np.zeros((n, n))
for i in range(n):
  for j in range(n):
    b[i, j] = k
    k += 1


c = a.dot(b)
print(a)
print(b)
print(c)

c = strassen_multiplication(a, b, n)
print("Result:")
print(c)


