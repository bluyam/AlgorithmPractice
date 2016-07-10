# Kyle Wilson
#
# Project Euler #8: Largest product in a series
# Finds the greatest product of K consecutive digits in the N digit number

import sys

def determine_max_consecutive_product(input_sequence, N, K):
    list = [int(i) for i in input_sequence[:N]]
    maximum = -sys.maxsize -1
    for section_start_index in range(N-K):
        consecutive_product = 1
        for value in list[section_start_index: section_start_index+K]:
            consecutive_product = consecutive_product * value
        if consecutive_product > maximum:
            maximum = consecutive_product
    print(maximum)

prev_line = []
for line in sys.stdin.readlines()[1:]:
    if len(line.split()) == 1:
        determine_max_consecutive_product(line, int(prev_line_split[0]), int(prev_line_split[1]))
    prev_line_split = line.split()
