#!/bin/python3

import sys
import math


t = int(input().strip())
# your code goes here

print((int)(t/2)*math.ceil(((t+1)/2)+1) if t%2==0 else (int)((((t+1)/2)*math.ceil(((t+2)/2)+1))-math.ceil((t+2)/2)))
