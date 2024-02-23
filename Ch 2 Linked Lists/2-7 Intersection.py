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


def intersection(head1, head2):
	tmp1, tmp2 = head1, head2
	# check if there is any intersection
	while tmp1.next is not None:
		tmp1 = tmp1.next
	while tmp2.next is not None:
		tmp2 = tmp2.next
	
	# check if there is any intersection
	if tmp1 != tmp2:
		return None

	size1 = findLength(head1)
	size2 = findLength(head2)
	s1 = head1 if size1 <= size2 else head2		# shorter LL
	s2 = head2 if size1 <= size2 else head1		# longer LL

	# if there is intersection
	# check if they are of the same size
	if size1 == size2:
		while s1 is not None:
			if s1 == s2:
				return s1.val

			s1 = s1.next
			s2 = s2.next

	# there is a size difference; find the intersecting node
	# by traversing the shorter LL (s1) by the difference
	else:	
		diff = abs(size1 - size2)

		while diff:
			s1 = s1.next
			diff -= 1

		return s1.val



head1 = LL(1)
head1.next = LL(2)
head1.next.next = LL(3)
head1.next.next.next = LL(4)
head1.next.next.next.next = LL(5)
show(head1)

head2 = LL(9)
head2.next = head1.next.next
# head2.next.next = LL(8)

show(head2)

print(intersection(head1, head2))