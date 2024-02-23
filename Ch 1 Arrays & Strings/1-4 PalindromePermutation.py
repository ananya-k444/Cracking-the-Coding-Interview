def palindromePermutation(s1, s2):
	if len(s1) != len(s2):
		return False

	hashmap = {}

	for i in s1:
		if i == ' ':
			continue

		if i in hashmap:
			hashmap[i] += 1
		else:
			hashmap[i] = 1

	for i in s2:
		if i == ' ':
			continue

		if i in hashmap:
			hashmap[i] -= 1
		else:  # when character is not present
			return False

		if hashmap[i] == 0:
			del hashmap[i]


	return False if len(hashmap) > 0 else True



s1 = "tact coa"
# s2 = "taco cat" 	# True
# s2 = "taco cct"		# False
# s2 = "atco cta"		# True
s2 = "btco cta"		# False
print(palindromePermutation(s1, s2))