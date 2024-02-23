def stringCompression(s):	# saving time, but extra space
	s_mod = str()
	count = 1
	i = 0

	while i < (len(s)-1):
		if s[i] != s[i+1]:
			s_mod = s_mod + s[i] + str(count)
			count = 1
		else:
			count += 1

		i += 1

	s_mod = s_mod + s[i] + str(count)

	return s_mod if len(s_mod)!=len(s) else s


def stringCompression2(s):	#  saving space, but extra time - 2 loops
	list_s = list(s)
	i = 0

	while i < len(list_s):
		count = 1
		
		while (i + count < len(list_s)) and (list_s[i] == list_s[i + count]):
			count += 1
			
		list_s[i: i+count] = list_s[i] + str(count)
		i += 2

	return ''.join(list_s) if len(list_s) != len(s)  else s


s = "aabcccccaaa" # a2b1c5a3
# s = "aabbccaa"	# as it is
print(stringCompression(s))