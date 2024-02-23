def pop(arr, stack_no, tops):
	if tops[stack_no-1] < (stack_no - 1) * (n // 3):
		print("Underflow condition")
		return -1

	popped_val = arr[ tops[stack_no-1] ]
	arr[ tops[stack_no-1] ] = -1
	tops[stack_no-1] -= 1

	return popped_val
	


def push(arr, stack_no, tops, ele):
	if tops[stack_no-1] == stack_no * ( n // 3 ) - 1:
		print("Overflow condition")
		return

	tops[stack_no-1] += 1
	arr[tops[stack_no-1]] = ele



def isEmpty(arr, stack_no, tops):
	if tops[stack_no-1] == (stack_no - 1) * ( n // 3 ) - 1:
		return True

	return False



def peek(arr, stack_no, tops):
	if isEmpty(arr, stack_no, tops):
		return -1

	return arr[tops[stack_no-1]]
	

n = 9
arr = [-1] * n
tops = [0-1, n // 3 - 1, 2 * (n // 3) - 1]

'''push'''
# push into stack 1
push(arr, 1, tops, 2)
# push into stack 2
push(arr, 2, tops, 3)
# push into stack 3
push(arr, 3, tops, 4)
print("arr= ", arr, "\ttops= ", tops)


# push into stack 1
push(arr, 1, tops, 4)
# push into stack 2
push(arr, 2, tops, 6)
# push into stack 3
push(arr, 3, tops, 8)
print("arr= ", arr, "\ttops= ", tops)


# push into stack 1
push(arr, 1, tops, 6)
# push into stack 2
push(arr, 2, tops, 9)
# push into stack 3
push(arr, 3, tops, 12)
print("arr= ", arr, "\ttops= ", tops)


'''peek'''
print("\nPeek stack 1: ", peek(arr, 1, tops))
print("Peek stack 2: ", peek(arr, 2, tops))
print("Peek stack 3: ", peek(arr, 3, tops))


'''is empty?'''
print("\nIs Empty stack 1: ", isEmpty(arr, 1, tops))
print("Is Empty stack 2: ", isEmpty(arr, 2, tops))
print("Is Empty stack 3: ", isEmpty(arr, 3, tops))


'''pop'''
print("\npopped from stack 1: ", pop(arr, 1, tops))
print("popped from stack 2: ", pop(arr, 2, tops))
print("popped from stack 3: ", pop(arr, 3, tops))
print("arr= ", arr, "\ttops= ", tops)

print("\npopped from stack 1: ", pop(arr, 1, tops))
print("popped from stack 2: ", pop(arr, 2, tops))
print("popped from stack 3: ", pop(arr, 3, tops))
print("arr= ", arr, "\ttops= ", tops)

print("\npopped from stack 1: ", pop(arr, 1, tops))
print("popped from stack 2: ", pop(arr, 2, tops))
print("popped from stack 3: ", pop(arr, 3, tops))
print("arr= ", arr, "\ttops= ", tops)


'''is empty?'''
print("\nIs Empty stack 1: ", isEmpty(arr, 1, tops))
print("Is Empty stack 2: ", isEmpty(arr, 2, tops))
print("Is Empty stack 3: ", isEmpty(arr, 3, tops))
