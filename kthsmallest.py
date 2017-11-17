class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, k):
        new_A = sorted(A)
        return new_A[k-1]