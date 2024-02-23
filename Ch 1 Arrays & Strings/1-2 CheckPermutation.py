def checkPermutation(s1, s2):
	if len(s1) != len(s2):
		return False

	hashmap = {}
	for i in s1:
		if i in hashmap:
			hashmap[i] += 1
		else:
			hashmap[i] = 1

	for i in s2:
		if i in hashmap:
			hashmap[i] += 1
		else:
			hashmap[i] = 1

	# print(hashmap.values())
	for count in list(hashmap.values()):
		if count % 2 == 1:
			return False

	return True


def checkPermutation2(s1, s2):
	if len(s1) != len(s2):
		return False

	s1 = sorted(list(s1))
	s2 = sorted(list(s2))

	for i in range(len(s1)):
		if s1[i] != s2[i]:
			return False

	return True


s1 = "abcde"
s2 = "acdeb"	# True
# s2 = "acdbf"	# False
print(checkPermutation2(s1, s2))