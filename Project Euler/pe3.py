import sys

def getMax(curMax, n):
    if n > curMax: return n
    else: return curMax

def getMaxFactor(maximum, n):
    i = 2
    while i * i - 1 < n:
        if n % i == 0:
            maximum = getMax(maximum, i)
            return getMaxFactor(maximum, n // i)
        i += 1
    maximum = getMax(maximum, n)
    return maximum

for line in sys.stdin.readlines()[1:]:
    n = int(line.split("\n")[0])
    print(getMaxFactor(0,n))
