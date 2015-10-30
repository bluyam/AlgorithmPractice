# Kyle Wilson
# pe5.py
#
# Smallest positive number divisible by every integer from 1 to input

import sys

for line in sys.stdin.readlines()[1:]:
    n = int(line.split("\n")[0])
    memory = []
    result = 1
    for number in range(1,n+1):
        additionalPrime = number
        for previousPrime in reversed(memory):
            if additionalPrime % previousPrime == 0:
                additionalPrime //= previousPrime
        result *= additionalPrime
        memory.append(additionalPrime)
    print(result)
