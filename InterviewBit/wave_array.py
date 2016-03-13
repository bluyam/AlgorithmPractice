class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort() # O(nlogn)
        n_pairs = len(A)/2
        for pair in range(0, n_pairs):
            index = pair*2
            A[index], A[index+1] = A[index+1], A[index]
        return A