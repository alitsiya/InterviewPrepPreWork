# Given a sorted array of integers, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example:

# Given [5, 7, 7, 8, 8, 10]

# and target value 8,

# return [3, 4].

def searchRange(A, B):

	#find left range
	l = 0
	r = len(A) - 1

	while l < r:
		m = (l + r) / 2
		if A[m] < B:
			l = m + 1
		else:
			r = m
	if A[l] == B:
		left_range = l
	else:
		left_range = -1

	#find right range
	l = 0
	r = len(A) - 1
	while l < r:
		m = (l + r + 1) / 2
		if A[m] > B:
			r = m - 1
		else:
			l = m
	if A[l] == B:
		right_range = r
	else:
		right_range = -1



	return [left_range, right_range]


print searchRange([5, 7, 7, 8, 8, 10], 8) # [3, 4]
print searchRange([4, 5, 6, 7, 8], 9) # [-1, -1]
A = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ]
print searchRange(A, 3) # [98, 140]


# Input : [4 5 6 7 0 1 2] and target = 4
# Output : 0
def returnIndex(lenA, shift, ind):

	return (ind + shift + 1) % lenA


def search(A, B):
	if len(A) == 0:
		return -1

	l = 0
	r = len(A) - 1

	while l < r:
		m = (l + r + 1) / 2
		if A[m] > A[l]:
			l = m
		else:
			r = m - 1
	# found shift

	shift = l

	l = 0
	r = len(A) - 1
	while l < r:
		m = (l + r) / 2
		if A[returnIndex(len(A), shift, m)] < B:
			l = m + 1
		else:
			r = m
	if A[returnIndex(len(A), shift, l)] == B:
		return returnIndex(len(A), shift, l)
	else:
		return -1



# print search([4, 5, 6, 7, 0, 1, 2], 4) 
# print search([4, 5, 6, 7, 0, 1, 2], 7)
# print search([4, 5, 6, 7, 0, 1, 2], 0)
# print search([4, 5, 6, 7, 0, 1, 2], 2)
# print search([4, 5, 6, 7, 0, 1, 2], -1)
# print search([4, 5, 6, 7, 0, 1, 2], 10)
# print search([0, 1, 2, 3, 4, 5, 6, 7], 2)
# print search([2, 3, 4, 5, 6, 1], 2)
# print search([2, 3, 4, 5, 6, 1], 7)
# print search([2, 3, 4, 5, 6, 1], 0)


