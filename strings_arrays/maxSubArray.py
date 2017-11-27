# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example:

# Given the array [-2,1,-3,4,-1,2,1,-5,4],

# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

# For this problem, return the maximum sum.

def maxSubArray(A):
	if len(A) == 0:
		return []
	if len(A) == 1:
		return A
	start = 0
	end = 1
	current = 1
	max_sum = 0

	while current < len(A):
		cur_sum = sum(A[start:current])
		if cur_sum > 0:
			if cur_sum > max_sum:
				max_sum = cur_sum
				end = current
		else:
			start = current + 1
			end = current + 1
		current += 1
	print max_sum
	


print maxSubArray([-2,1,-3,4,-1,2,1,-5,4])