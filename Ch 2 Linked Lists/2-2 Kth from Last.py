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


# finding the size, then the (size - k)th node
def kthToLast(head, k):
	size = findLength(head)

	if k > size:
		return None

	tmp = head
	tmp_k = size - k
	while tmp_k:
		tmp = tmp.next
		tmp_k -= 1

	return tmp.val


# iteratively with two pointers
def kthToLast2(head, k):
	p1 = p2 = head
	tmp_k = k

	while tmp_k-1:
		p2 = p2.next
		if p2 is None: 
			return None
		tmp_k -=1

	while p2.next is not None:
		p1 = p1.next
		p2 = p2.next

	return p1.val


# recursion
def kthToLast3(head, k):
	pass


head = LL(1)
head.next = LL(2)
head.next.next = LL(3)
head.next.next.next = LL(4)
# head.next.next.next.next = LL(5)
# head.next.next.next.next.next = LL(6)
# head.next.next.next.next.next.next = LL(7)
# head.next.next.next.next.next.next.next = LL(8)
# head.next.next.next.next.next.next.next.next = LL(9)
show(head)

k = 4
print("Kth element from the last: ", kthToLast(head, k))