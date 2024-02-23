class LL:
	def __init__(self, val = 0):
		self.val = val
		self.next = None


def show(head):
	tmp = head
	while tmp != None:
		print(tmp.val, end=' -> ')
		tmp = tmp.next
	print("!!!")


# remove duplicates in an unsorted Linked List
def removeDups(head):
	if (head is None) or (head.next is None):
		return 

	tmp = head
	hashmap = [tmp.val]

	while (tmp is not None) and (tmp.next is not None):
		if tmp.next.val not in hashmap:
			hashmap.append(tmp.next.val)
		else:	# duplicate is found
			tmp2 = tmp.next
			while (tmp2 is not None) and (tmp2.val in hashmap):		# handle adjacent duplicates
				tmp2 = tmp2.next

			if tmp2 is not None:
				hashmap.append(tmp2.val)

			tmp.next = tmp2

		tmp = tmp.next


# head = LL(7)
# head.next = LL(2)
# head.next.next = LL(9)
# head.next.next.next = LL(5)
# head.next.next.next.next = LL(9)
# head.next.next.next.next.next = LL(2)
# head.next.next.next.next.next.next = LL(1)
# head.next.next.next.next.next.next.next = LL(3)
# head.next.next.next.next.next.next.next.next = LL(3)
# head.show()


head2 = LL(7)
head2.next = LL(7)
head2.next.next = LL(1)
show(head2)


print("\nAfter removing the duplicates: ")
removeDups(head2)
show(head2)