def isEmpty(st):
	if len(st) == 0:
		return True
	return False


def peek(st):
	if isEmpty(st):
		return -1
	return st[-1]


def showStack(st):
	i = len(st) - 1
	while i >= 0:
		print(st[i][0], end=' -> ')
		i -= 1
	print("!!!")


def push(st, val):
	if isEmpty(st):
		st.append([val, val])	# [val, minm]
	else:
		minm = min(peek(st)[1], val)
		# print("minm: %d, val: %d" % (minm, val))
		st.append([val, minm])


def pop(st):
	if len(st):
		return st.pop()


st = []
array = [2, 4, 1, 5, 3]
i = 0

# pushing into stack
while i < len(array):
	push(st, array[i])
	i += 1

# minm val when popping
while not isEmpty(st):
	showStack(st)
	print("Minimum val in stack: ", peek(st)[1])
	print()	
	pop(st)
