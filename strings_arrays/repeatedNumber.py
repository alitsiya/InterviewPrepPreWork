def repeatedNumber(A):
    dic = {}
    for item in A:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    for item in dic:
        if dic[item] > 1:
            return item
    return -1