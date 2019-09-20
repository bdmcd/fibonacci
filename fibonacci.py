import sys
import time
import math
import numpy as np
import json

n = int(sys.argv[1])
cache_file = "cache.json"
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


def getPowers(logn):
     pows = None
     with open(cache_file, 'a+') as _: _ = None
     with open(cache_file, 'r+') as infile:
          try:
               pows = json.load(infile)['powers']
          except:
               pows = []

     A = [[1, 1],
          [1, 0]]

     l = len(pows)
     for i in range(logn - l):
          k = i + l
          pows.append(matrix_power(A, 2 ** k))

     with open(cache_file, 'w') as outfile:
          cache_data = {}
          cache_data['powers'] = pows
          json.dump(cache_data, outfile)

     return pows

def fib3(n): #log(n)
     print("Calculating.....")
     if (n == 0): return 0
     if (n == 1): return 1

     logn = None
     if (n >= 2):
          logn = int(math.ceil(math.log(n + 1, 2)))
     pows = getPowers(logn)

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


start3 = time.time()
f3 = fib3(n)
end3 = time.time()
t3 = end3 - start3

print("fib(%s): %s\ntime=%s" % (n, f3, t3))
