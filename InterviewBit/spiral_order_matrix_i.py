class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        result = []
        ## Actual code to populate result
        
        ##########################################
        # 1) INITIALIZE 
        ##########################################
        m = len(A)-1
        n = len(A[0])-1
        top = 0
        left = 0
        bottom = m
        right = n
        d = 0
        
        ##########################################
        # 2) SPIRAL TRAVERSE
        ##########################################
        while (top <= bottom and left <= right):
            if d == 0:
                # go right
                for i in range(left, right+1):
                    result.append(A[top][i])
                top+=1
            elif d == 1:
                # go down
                for i in range(top, bottom+1):
                    result.append(A[i][right])
                right-=1
            elif d == 2:
                # go left
                for i in range(right, left-1, -1):
                    result.append(A[bottom][i])
                bottom-=1
            elif d == 3:
                # go up
                for i in range(bottom, top-1, -1):
                    result.append(A[i][left])
                left+=1
            d = (d + 1) % 4
        return result
