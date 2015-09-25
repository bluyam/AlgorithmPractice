import sys

def isSixDigitPalindrome(n):
    if n//1000 == (n%10)*99 + (n%100) + ((n%1000)-(n%100))//100:
        return True
    else:
        return False

print(isSixDigitPalindrome(100001))


list = {}
# for n in range (input/1000, 100, -1)
# palindrome from n = n*1000 + (n%10)*99 + (n%100) + (n//100)

for line in sys.stdin.readlines()[1:]:
    n = int(line.split("\n")[0])

def switch(x):
