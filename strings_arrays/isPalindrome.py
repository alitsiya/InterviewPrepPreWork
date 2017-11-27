def isPalindrome(A):
	letters = "0123456789abcdefghijklmnopqrstuvwsyz"
	a = A.lower()
	new_a = ""
	for letter in a:
		if letter in letters:
			new_a += letter
	for i in range(len(new_a)/2):
		if new_a[i] != new_a[-1-i]:
			return 0
	return 1

print isPalindrome("A time T")
print isPalindrome("A man, a plan, a canal: Panama")
print isPalindrome("1a2")