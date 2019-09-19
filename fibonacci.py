import sys
import time
import math
import numpy as np

n = int(sys.argv[1])
print("Calculating fibonacci number %s\n" % n)
if (n < 0):
     print("Must be greater than or equal to 0")
     exit()

def matrix_multiply(a, b):  # look into using the more efficient n^2.81 algorithm
     rowsA = len(a)
     if (rowsA == 0): return
     rowsB = len(b)
     if (rowsB == 0): return
     colsA = len(a[0])
     if (colsA == 0): return
     if (colsA != rowsB):
          print("Incorrect format")
          return
     colsB = len(b[0])
     if (colsB == 0): return

     c = []
     for ra in range(rowsA):
          cc = []
          for nb in range(colsB):
               nc = 0
               for na in range(colsA):
                    nc += a[ra][na] * b[na][nb]
               cc.append(nc)
          c.append(cc)
     return c

def matrix_power(a, n): # doesn't work for 0th power (identity matrix)
     lenA = len(a)
     if (lenA == 0 or lenA != len(a[0])):
          return

     b = a
     if (n == 0):
          for i in range(lenA):
               for j in range(lenA):
                    if (i == j): 
                         b[i][j] = 1
                    else: 
                         b[i][j] = 0
     else:
          for i in range(n - 1):
               b = matrix_multiply(b, a)
     return b

def fib1(n): #exponential
     if (n == 0): return 0
     if (n == 1): return 1
     return fib1(n-1) + fib1(n-2)

def fib2(n): #polynomial
     if (n == 0): return 0
     if (n == 1): return 1
     f = [0, 1]

     for x in range(2, n + 1):
          f.append(f[x-1] + f[x-2])

     return f[n]

print("calculating matrices")
A = [[1, 1],
     [1, 0]]

pows = []
logn = 0
if (n >= 2):
     logn = int(math.ceil(math.log(n + 1, 2)))

for i in range(logn):
     pows.append(matrix_power(A, 2 ** i))

def fib3(n): #log(n)
     if (n == 0): return 0
     if (n == 1): return 1

     
     B = None
     if (logn == 0): B = A
     for i in range(logn):
          k = 2 ** i
          if (k & n):
               if (B is None): B = pows[i]
               else: B = matrix_multiply(B, pows[i])

     C = matrix_multiply(B, [[0],[1]])
     return C[0][0]


def fib4(n):
     sqrt5 = math.sqrt(5)
     return (((1 + sqrt5) ** n) - ((1 - sqrt5) ** n)) / ((2**n) * sqrt5)

# start1 = time.time()
# f1 = fib1(n)
# end1 = time.time()
# t1 = end1 - start1

print("starting fib3")

start2 = 0#time.time()
f2 = 0#fib2(n)
end2 = 0#time.time()
t2 = 0#end2 - start2

start3 = time.time()
f3 = fib3(n)
end3 = time.time()
t3 = end3 - start3

# start4 = time.time()
# f4 = fib4(n)
# end4 = time.time()
# t4 = end4 - start4

print("fib2: %s, time=%s\n\nfib3: %s, time=%s" % (f2, t2, f3, t3))