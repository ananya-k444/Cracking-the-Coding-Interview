class LL:
	def __init__(self, val):
		self.val = val
		self.next = None


def show(head):
	tmp = head
	while tmp != None:
		print(tmp.val, end=' -> ')
		tmp = tmp.next
	print("!!!")


def findLength(head):
	tmp = head
	size = 0
	while tmp is not None:
		size += 1
		tmp = tmp.next

	return size


# finding the size and using stack
def palindrome(head):
	size = findLength(head)
	stack = []
	tmp = head
	i = 0

	while i < size//2:
		stack.append(tmp.val)
		tmp = tmp.next
		i += 1

	if size % 2 == 1:
			tmp = tmp.next

	while tmp:
		if stack[-1] != tmp.val:
			return False

		stack.pop()
		tmp = tmp.next

	return False if len(stack) else True



# head = LL(1)
# head.next = LL(2)
# head.next.next = LL(3)
# head.next.next.next = LL(4)
# head.next.next.next.next = LL(3)
# head.next.next.next.next.next = LL(2)
# head.next.next.next.next.next.next = LL(1)	# size = 7 odd
# show(head)

# head2 = LL(3)
# head2.next = LL(2)
# head2.next.next = LL(1)
# head2.next.next.next = LL(1)
# head2.next.next.next.next = LL(2)
# head2.next.next.next.next.next = LL(3)	# size 6 - even
# show(head2)

head3 = LL(3)
head3.next = LL(2)
head3.next.next = LL(1)
head3.next.next.next = LL(5)
head3.next.next.next.next = LL(2)
head3.next.next.next.next.next = LL(3)	# size 6 - even
show(head3)

print(palindrome(head3))