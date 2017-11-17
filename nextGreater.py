class Solution:
    # @param A : list of integers
    # @return a list of integers
    def findNext(self, A, i):
        for j in range(i + 1, len(A)):
            if A[j] > A[i]:
                return A[j]
        return -1
        
    def nextGreater(self, A):
        for i in range(len(A)):
            if i == len(A) - 1:
                A[i] = -1
            A[i] = self.findNext(A, i)
        return A