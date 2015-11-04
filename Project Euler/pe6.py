import sys

def sumSquare(n):
    return sum(map(lambda x: x*x, range(n+1)[1:]))

def squareSum(n):
    return (n*(n+1)//2)*(n*(n+1)//2)

def sumSquareDiff(n):
    return squareSum(n) - sumSquare(n) 

for line in sys.stdin.readlines()[1:]:
    n = int(line.split("\n")[0])
    print(sumSquareDiff(n))
