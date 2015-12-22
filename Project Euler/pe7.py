# Kyle Wilson
#
# Project Euler #7: 10001st Prime
# Returns nth prime number for n < 10001

import sys

def P(): 
    p = []
    for i in [3,7]:
        p.append(i)
    for i in range(10, 104730):
        if (i%10==1 or i%10==3 or i%10==7 or i%10==9):
            isPrime = True
            for j in p:
                if i%j == 0:
                    isPrime = False
                    break
            if isPrime:
                p.append(i)
    p.insert(0,2)
    p.insert(2,5)
    return p

primes = P()

for line in sys.stdin.readlines()[1:]:
    n = int(line.split("\n")[0])
    print(primes[n-1])
