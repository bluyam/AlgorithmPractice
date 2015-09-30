import sys

def isProdOfThree(p):
    for f in range(100, 1000):
        if p % f == 0 and p // f < 1000 and p // f > 99:
            return True
            break
    return False

for line in sys.stdin.readlines()[1:]:
    palindromes = []
    n = int(line.split("\n")[0])
    prefix = n//1000
    if n <= (prefix*1000 + (prefix%10)*99 + (prefix%100) + (prefix//100)):
        limit = n//1000
    else:
        limit = n//1000 + 1
    for half in reversed(range(100, limit)):
        palindromes.append(half*1000 + (half%10)*99 + (half%100) + (half//100))
    for p in palindromes:
        if isProdOfThree(p):
            print(p)
            break
