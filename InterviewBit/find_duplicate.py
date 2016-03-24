class Solution:
    # @param A : tuple of integers
    # @return an integer
    # O(n) time, O(1) space (if array is modifiable)
    # Admittedly, there's no way I would've figured this out
    # Without the help of Google.
    # Since the values in the array are from 1-n, we can flag
    # the values at indices which correspond to the visited elements
    # If the flag exists at an index, that index represents a duplicate value
    def repeatedNumber(self, A):
        L = list(A)
        for i in range(0,len(L)):
            j = abs(L[i])
            if L[j] > 0:
                L[j] = -(L[j])
            else: 
                return j