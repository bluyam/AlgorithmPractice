class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
    	# counts the number of unique factors of five
    	# which is the same as the number of unique factors of ten
    	# which is the same as the number of trailing zeros!
    	# running time is O(logn), with base 5 to be exact
        A = A - (A%5)
        answer = 0
        while A >= 5:
            A = A/5
            answer += A
        return answer