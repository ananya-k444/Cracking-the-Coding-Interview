def pop(st):
	if len(st):
		return st.pop()


def push(st, val):
	st.append(val)


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


def sortStack(st1):
	if isEmpty(st1):
		return

	st2 = []

	# move all the contents to the buffer stack
	while not isEmpty(st1):
		if isEmpty(st2):
			push(st2, pop(st1))
		while peek(st1) >= peek(st2):
			push(st2, pop(st1))

		tmp = pop(st1)

		if tmp:
			while peek(st2) > tmp:
				push(st1, pop(st2))

			push(st2, tmp)			

	# transfer the asc order array from buffer to original
	while not isEmpty(st2):
		push(st1, pop(st2))

	print("Final modified stack: ", end='')
	showStack(st1)


st = [1, 1, 1]
print("Original stack: ", end='')
showStack(st)

# call the function here
sortStack(st)