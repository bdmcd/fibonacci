import math
import json
import cache
import matrix

# **************** EXPONENTIAL ALGORITHM ****************
def fib_exp(n):
     if (n == 0): return 0
     if (n == 1): return 1
     return fib1(n-1) + fib1(n-2)



# **************** POLYNOMIAL ALGORITHM ****************
def fib_poly(n):
     if (n == 0): return 0
     if (n == 1): return 1
     f = [0, 1]

     for x in range(2, n + 1):
          f.append(f[x-1] + f[x-2])

     return f[n]



# **************** LOGARITHMIC ALGORITHM ****************
def calculateMatrixPowers(logn):
     powers = cache.get_cached_powers()
     
     A = [[1, 1],
          [1, 0]]

     l = len(powers)
     for i in range(logn - l):
          k = i + l
          powers.append(matrix.matrix_power(A, 2 ** k))

     cache.save_cached_powers(powers)
     return powers

def fib_log(n):
     if (n == 0): return 0
     if (n == 1): return 1

     logn = None
     if (n >= 2):
          logn = int(math.ceil(math.log(n + 1, 2)))
     powers = calculateMatrixPowers(logn)

     B = None
     if (logn == 0): B = A
     for i in range(logn):
          k = 2 ** i
          if (k & n):
               if (B is None): B = powers[i]
               else: B = matrix.matrix_multiply(B, powers[i])

     C = matrix.matrix_multiply(B, [[0],[1]])
     return C[0][0]


