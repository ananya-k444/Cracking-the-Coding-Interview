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
		print(st[i], end=' -> ')
		i -= 1
	print("!!!")


def push(st, st_min, val):
	if isEmpty(st):
		st.append(val)
		st_min.append(val)
	else:
		st.append(val)
		minm = min(peek(st_min), val)
		if peek(st_min) != minm:
			st_min.append(minm)


def pop(st, st_min):
	if len(st):
		popped = st.pop()
		if popped == peek(st_min):
			st_min.pop()

	return popped


st = []
st_min = []
array = [2, 4, 1, 5, 3]
i = 0

# min value when pushing into stack
while i < len(array):
	push(st, st_min, array[i])
	# print("st: ", end='')
	showStack(st)

	# print("st_min: ", end='')
	# showStack(st_min)
	print("minimum value: ", peek(st_min))
	# print()

	i += 1


# min value when popping
print()
while not isEmpty(st):
	showStack(st)
	print("minimum value: ", peek(st_min))
	pop(st, st_min)