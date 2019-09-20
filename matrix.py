# TODO: look into using the more efficient n^2.81 algorithm
def matrix_multiply(a, b):
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

# TODO: doesn't work for 0th power (should give the identity matrix)
def matrix_power(a, n):
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