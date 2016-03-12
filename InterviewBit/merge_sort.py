# Best Case: Sorted Array, O(n)
# Worst Case: Reversed Array, O(n^2)
# Average Case: O(n^2)
# Space Complexity: O(n) [the two subarrays/limit to 2n]

def merge_sort(A):
	# base case
	n = len(A)
	if n < 2:
		return A
	mid = n/2
	# divide into two
	# recursive call on the two sublists
	L = merge_sort(A[0:mid])
	R = merge_sort(A[mid:])
	# merge the results
	return merge(L,R)

def merge(L,R):
	# pull the lowest number card from the top of the deck
	result = []
	n_l = len(L)
	n_r = len(R)
	i = 0
	j = 0
	while True:
		if L[i] <= R[j]:
			result.append(L[i])
			i += 1
			if i >= n_l:
				result.extend(R[j:])
				break
		else:	
			result.append(R[j])
			j += 1
			if j >= n_r:
				result.extend(L[i:])
				break
	return result
