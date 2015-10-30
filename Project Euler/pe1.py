import sys

def sumForFactor(f, n): # f is the factor, n is the input
    return f*((n-1)//f)*(((n-1)//f)+1)//2 # determines the sum of all the multiples of a factor up to but not including n

for line in sys.stdin.readlines()[1:]:
    n = int(line.split("\n")[0])
    print(sumForFactor(3,n)+sumForFactor(5,n)-sumForFactor(15,n))
    
