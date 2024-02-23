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


# delete within except 
def deleteWithin(head, mid):
	if mid == head or mid.next is None:
		return

	tmp = head.next
	while tmp.next != mid:
		tmp = tmp.next

	tmp.next = mid.next


head = LL(1)
head.next = LL(2)
head.next.next = LL(3)
head.next.next.next = LL(4)
head.next.next.next.next = LL(5)
head.next.next.next.next.next = LL(6)	
show(head)

# deleteWithin(head, head)	# 1
# deleteWithin(head, head.next.next.next)	# 4
deleteWithin(head, head.next.next.next.next)	# 5
# deleteWithin(head, head.next.next.next.next.next)	# 6
print("After modifiction:")
show(head)