class Solution:
    # @param A : list of integers
    # @return a list of integers
    # Solution is O(n)
    
    def plusOne(self, A):
        # first, strip excess 0s from array (loop fwd)
        n = len(A)
        value = n
        for i in range(0,n):
            if A[i] == 0:
                continue
            else:
                value = i
                break
        answer = A[n-1:] if value == n else A[i:n]
        n = len(answer)
        
        #second, implement addition for arrays (loop bkwd)
        carry = True 
        for i in range(n-1, -1, -1):
            if answer[i] == 9 and carry:
                answer[i] = 0
                carry = True
            elif carry:
                answer[i] += 1
                carry = False
            else:
                break
        if carry:
            answer.insert(0,1)
        return answer
