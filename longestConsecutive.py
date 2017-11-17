class Solution:
    # @param A : tuple of integers
    # @return an integer

    def longestConsecutive(self, A):
        d = {}
        for i in range(len(A)):
            if A[i] in d:
                continue
            else:
                d[A[i]] = False
                
        max_seg = -1
        for i in d:
            if d[i] == False:
                curr = i+1; len_right = 0
                while curr in d:
                    len_right += 1
                    d[curr] = True
                    curr += 1
                curr = i-1
                len_left = 0
                while curr in d:
                    len_left += 1; d[curr] = True; curr -= 1
                max_seg = max(max_seg, len_left+1+len_right)
        return max_seg