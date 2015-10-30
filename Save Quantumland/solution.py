#!/bin/python3

# Kyle Wilson
# Codestorm 2015 Challenge 2
# Save Quantumland

import sys


# number of guards needed per number of adjacent empty spots
def guardsPerEmpties(empties):
    return 0 if empties == 1 else empties//2

# read input
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a = [int(a_temp) for a_temp in input().strip().split(' ')]

    adjEmptyAcc = 0 # accumulator for number of adjacent empties
    minGuards = 0 # the result

    for x in a:
        if (x == 0): # add empty to accumulator
            adjEmptyAcc += 1
        else: # calculate guardsPerEmpties for the last series of empties
            minGuards += guardsPerEmpties(adjEmptyAcc)
            adjEmptyAcc = 0 # reset
    minGuards += guardsPerEmpties(adjEmptyAcc) # accounts for sequences with 2+ empties at the end

    print(minGuards) # print solution
