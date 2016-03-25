class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    
    def nth_digit(self, A, N):
        # returns the nth digit of a number
        # for example, in 192, 9 would be the 1st digit
        # and 2 would be the 0th digit
        return (A%int(math.pow(10,N+1)))/int(math.pow(10,N))
    
    def isPalindrome(self, A):
        # negative numbers are not considered palindromes
        if A < 0:
            return False
        # Step 1) Determine the length of the integer
        length = 0 
        while(True):
            divisor = math.pow(10,length)
            if A/divisor < 1:
                break
            length += 1
        # Step 2) Compare both ends to validate
        for i in range(0,length/2):
            if self.nth_digit(A, i) != self.nth_digit(A, length-1-i):
                return False
        return True