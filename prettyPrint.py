class Solution:
    # @param A : integer
    # @return a list of list of integers
    
    def prettyPrint(self, A):
        arr_len = A*2 - 1
        arr = [0]*(arr_len)
        for i in range(arr_len):
            arr[i] = [0]*(arr_len)
        z = A
        while z >= 1:
            diff = abs(z-A)
            for i in range(0 + diff, arr_len - diff):
                arr[0 + diff][i] = A - diff
                arr[-1 - diff][i] = A - diff
                arr[i][0 + diff] = A - diff
                arr[i][-1 - diff] = A - diff
            z -= 1
    
        return arr