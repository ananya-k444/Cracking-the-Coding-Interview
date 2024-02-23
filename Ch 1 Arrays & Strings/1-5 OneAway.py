def oneAway(s1, s2):
	setdiff = (set(s1) - set(s2)).union(set(s2) - set(s1))
	# print(setdiff)

	if ( abs(len(s1) - len(s2)) <= 1 ) and ( len(setdiff) <= 2 ):
		return True

	return False



def oneAway2(first, second):
	# Length check
	if abs(len(first)-len(second)) > 1:
		return False

	s1 = first if len(first) <= len(second) else second		# shorter as the first string
	s2 = first if len(first) > len(second) else second		# longer as the second string

	index1 = index2 = 0
	foundDifference = False

	while ( (index1 < len(s1)) and (index2 < len(s2)) ):
		if ( s1[index1] != s2[index2] ):
			if foundDifference:		# if foundDifference again, >1 changes made: return False3
				return False
			foundDifference = True

			# 1. replace condition (same lengths): move the first pointer, second pointer is incremented later
			# 2. if lengths are different, there might be another edit (extra length, 
			# apart from the non-matched characters - if condition)
			if len(s1) == len(s2):	
				index1 += 1

		# if same characters - move both the pointers outside (else part and index2)
		else:	
			index1 += 1

		index2 += 1	# always move pointer for the longer string

	return True



s1 = "pale"

s2 = "ple"		# True  [-1 & setdiff={a}]
# s2 = "bale"		# True  [0 & setdiff={p, b}]
# s2 = "bales"	# False  [+1 & setdiff={p, b, s}]
# s2 = "bake"		# False  [0 & setdiff={p, b, l, k}]
# s2 = "bae"
print(oneAway2(s1, s2))