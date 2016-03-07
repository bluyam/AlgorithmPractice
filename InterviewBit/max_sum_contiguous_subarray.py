import sys

class Solution:
    # @param A : tuple of integers
    # @return an integer
    # let's use dynamic programming! :D
    # solution is O(nlogn)
    
    # primary function (recursive)
    def maxSubArray(self, A):
        n = len(A)
        # base case
        if n == 1:
            return A[0]
        # divide
        m = (n)/2
        l = A[0:m]
        r = A[m:n]
        # conquer
        return max(self.maxSubArray(l),
                   self.maxSubArray(r),
                   self.maxOverlappingSum(A,m))
    
    # find the maximum sum including A[m]
    def maxOverlappingSum(self, A, m):
        n = len(A)
        
        # leftward summation
        sum_temp = 0
        sum_l = -sys.maxint-1
        for i in range(m-1, -1, -1):
            sum_temp += A[i]
            sum_l = sum_temp if sum_l < sum_temp else sum_l
        
        # rightward summation
        sum_temp = 0
        sum_r = -sys.maxint-1 
        for i in range(m, n):
            sum_temp += A[i]
            sum_r = sum_temp if sum_r < sum_temp else sum_r
            
        return sum_l + sum_r
        
        