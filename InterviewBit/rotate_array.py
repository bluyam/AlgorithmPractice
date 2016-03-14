class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        # Step 1) Transpose
        for i in range(0, n-1):
            for j in range(0, n-i-1):
                A[i][j], A[n-1-j][n-1-i] = A[n-1-j][n-1-i], A[i][j]
        # Step 2) Flip
        n_flips = n/2
        for i in range(0, n_flips):
            for j in range(0, n):
                A[i][j], A[n-i-1][j] = A[n-i-1][j], A[i][j]
        return A