def isSubstring(s1, s2, idx, size):
	for i in range(size):
		if s1[i] != s2[(i+idx) % size]:
			return False
			
	return True

def stringRotation(s1, s2):
	if len(s1) != len(s2):
		return False

	size = len(s1)
	firstChar = s1[0]
	indexes = []
	for i in range(size):
		if firstChar == s2[i]:
			indexes.append(i)

	for idx in indexes:
		if isSubstring(s1, s2, idx, size):
			return True

	return False


s1 = "waterbottle"
s2 = "terbottlewa"
print(stringRotation(s1, s2))