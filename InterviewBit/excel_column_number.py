class Solution:
    # @param A : string
    # @return an integer
    # base conversion; O(n) where n is the length of the string
    def titleToNumber(self, A):
        n = len(A)
        answer = 0
        for i in range(0, n):
            digit = A[i]
            answer += (ord(digit)-64)*math.pow(26,n-i-1)
        return int(answer)