# Divide and conquer, but in place
# Best/Average case: O(nlogn) - most practical
# Worst case: O(n^2) - can be avoided by using randomized qs
# In-place; Space complexity: O(1)
def quick_sort(A, start, end):
	# base case: do nothing if start >= end
	# rearrange elements around some pivot
	# pass subarray indices to quick_sort
	# return nothing; in-place
	if start < end:
		index = partition(A, start, end)
		quick_sort(A, start, index - 1)
		quick_sort(A, index + 1, end) # + 1 because we're skipping the pivot

# Helper function which sets a pivot for quick_sort()
def partition(A, start, end):
	pivot = A[end]
	index = start
	for i in range(start, end):
		if A[i] <= pivot:
			A[i], A[index] = A[index], A[i]
			index += 1
	A[index], A[end] = A[end], A[index]
	return index