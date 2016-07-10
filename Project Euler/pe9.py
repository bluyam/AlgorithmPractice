# Kyle Wilson
#
# Project Euler #9: Special Pythagorean triplet
# Given N, Check if there exists any Pythagorean triplet for which a+b+c = N 
import sys

def pe9(x):
    # there are no odd triple sums
    if x % 2 == 1:
        return -1
    b = (x/2)-1
    triple_prods = []
    while True:
        # derived from a + b + c = N and pythagorean theorem substitution on c
        a = (x*x/2 - x*b)/(x - b)
        if b < 1:
            break
        if a % 1 == 0:
            triple_prods.append(int(a*b*(x-a-b)))
        b = b - 1
    return -1 if not triple_prods else max(triple_prods)

for line in sys.stdin.readlines()[1:]:
    print(pe9(int(line)))