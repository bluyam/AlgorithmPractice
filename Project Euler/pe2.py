# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def fib(a, b, sumHolder, limit):
    if a%2==0: sumHolder+=a
    if b>limit: return sumHolder
    else: return fib(b, a+b, sumHolder, limit)

for line in sys.stdin.readlines()[1:]:
    n = int(line.split("\n")[0])
    print fib(1, 2, 0, n)
    
