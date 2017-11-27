def plusOne(A):
	st = ""
	for item in A:
		st += str(item)
	print int(st) + 1

plusOne([1, 2, 3])
plusOne([0, 1, 2, 3])
plusOne([0])