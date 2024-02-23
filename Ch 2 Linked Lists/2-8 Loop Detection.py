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


def ifLoop(head):
	turtle = head
	hare = head.next

	while hare.next and hare.next.next:
		turtle = turtle.next
		hare = hare.next.next

		if turtle == hare:
			return True

	return False


def loopDetectionNode(head):
	if ifLoop(head):
		hashmap = []

		tmp = head

		while tmp:
			if tmp.val not in hashmap:
				hashmap.append(tmp.val)
			else:
				return tmp.val
			tmp = tmp.next
	else:
		return None



head = LL('A')
head.next = LL('B')
head.next.next = LL('C')
head.next.next.next = LL('D')
head.next.next.next.next = LL('E')
head.next.next.next.next.next = head.next.next
# head.next.next.next.next.next.next = LL(7)
# show(head)

print(loopDetectionNode(head))