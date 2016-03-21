import math

class Solution:
    # @param A : integer
    # @return a boolean
    # O(logn)
    def isPower(self, A):
        if A < 2:
            return 1
        lim = int(math.log(A,2))
        for i in range(2, lim+1):
            root = math.pow(A,1/float(i))
            if root%1 > 0.9999 or root%1 == 0.0:
                return True
        return False