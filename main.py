import sys
import time
import fibonacci

# TODO: Print a better usage message.  Add a -help option
def usage():
     print("Incorrect usage!")

def nth(n):
     if n == 1: return 'st'
     if n == 2: return 'nd'
     if n == 3: return 'rd'
     return 'th'

# TODO: Add ability to choose which algorithm to use
def evaluate(n):
     print("\nCalculating the %s%s fibonacci number..." % (n, nth(n)))
     print("----------------------------------------\n")

     startTime = time.time()
     fibonacciNumber = fibonacci.fib_log(n)
     endTime = time.time()
     timeTaken = endTime - startTime
     
     print("The %s%s fibonacci number is: %s\n" % (n, nth(n), fibonacciNumber))
     print("It took about %s seconds to calculate\n" % timeTaken)

try:
     n = int(sys.argv[1])
     try: evaluate(n)
     except Exception as e: print(e)
except Exception as usageError:
     print(usageError)
     usage()
     exit()