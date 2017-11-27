def lengthOfLastWord(A):
 	arr = A.split()
 	return len(arr[-1])

print lengthOfLastWord("Hello World")