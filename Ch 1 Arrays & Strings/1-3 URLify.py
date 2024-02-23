def URLify(s):
	s = s.strip()
	modif = []

	for i in s:
		if i == ' ':
			modif.append("%20")
		else:
			modif.append(i)

	return ''.join(modif)


## can be done better in Java, C++
def URLify2(s, trueLength):
	if trueLength < len(s):
		s = s[:trueLength] + '\0'

	spaces = 0
	for i in s:
		if i == '\0': 
			break
		if i == ' ':
			spaces += 1

	index = trueLength + spaces * 2
	modif_s = list([0] * index)
	modif_s[index-1] = '\0'

	for i in range(trueLength-1, -1, -1):
		if s[i] == ' ':
			modif_s[index-1] = '0'
			modif_s[index-2] = '2'
			modif_s[index-3] = '%'
			index -= 3
		else:
			modif_s[index-1] = s[i]
			index -= 1

	return ''.join(modif_s)



s = "Mr John Smith   "
print(URLify2(s, 13))