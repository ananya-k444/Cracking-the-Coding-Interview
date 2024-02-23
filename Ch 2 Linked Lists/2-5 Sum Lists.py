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


def insertEndLL(head):
	pass


def sumLists(head1, head2):
	tmp1, tmp2 = head1, head2
	final_head = f_tmp = None
	sums = rem = 0

	while tmp1 and tmp2:
		sums = tmp1.val + tmp2.val
		# print(sums % 10 + rem)
		node = LL(sums % 10 + rem)

		if final_head is None:
			final_head = f_tmp = node
		else:
			f_tmp.next = node
			f_tmp = f_tmp.next

		rem = sums // 10

		tmp1 = tmp1.next
		tmp2 = tmp2.next

	
	if (tmp1 is None) and (tmp1 is None) and rem:
		node = LL(rem)
		f_tmp.next = node
	else:
		tmp = tmp1 if tmp1 else tmp2

		while tmp:
			node = LL(tmp.val + rem)
			rem = 0
			f_tmp.next = node

			f_tmp = f_tmp.next
			tmp = tmp.next


	return final_head


# FOLLOW UP - the digits are in reversed order from before
def sumLists2(head1, head2):
	# insert new node in the BEGINNING
	pass


head1 = LL(7)
head1.next = LL(1)
head1.next.next = LL(9)
head1.next.next.next = LL(1)
# head1.next.next.next.next = LL(2)
show(head1)

head2 = LL(5)
head2.next = LL(9)
head2.next.next = LL(2)		# 617 + 295 = 912. Final LL: 2 -> 1 -> 9 -> !!!
show(head2)

final_head = sumLists(head1, head2)
print()
show(final_head)