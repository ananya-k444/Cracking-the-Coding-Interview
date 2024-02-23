class Queue:
	def __init__(self):
		self.s1 = []
		self.s2 = []


	def add(self, ele):
		if len(self.s2) != 0:
			while len(self.s2):
				self.s1.append(self.s2.pop())

		self.s1.append(ele)
		

	def remove(self):
		if not len(self.s1) and not len(self.s2):
			return -1

		if len(self.s1):	# s1 is full, transfer everything to s2
			while len(self.s1):
				self.s2.append(self.s1.pop())

		return self.s2.pop()


	def peek(self):		# front element
		if self.isEmpty():
			return -1

		if not len(self.s2):		# move everything from s1
			while len(self.s1):
				self.s2.append(self.s1.pop())

		return self.s2[-1]


	def isEmpty(self):
		if not len(self.s1) and not len(self.s2):
			return True

		return False



q = Queue()


print(q.s1, q.s2)
q.add(1)
q.add(2)
q.add(3)
q.add(4)
q.add(5)

print(q.s1, q.s2)

print("\na")
q.remove()
print(q.s1, q.s2)

print("\nb")
q.add(6)
q.add(7)
print(q.s1, q.s2)

print("\nc")
print(q.peek())
print(q.s1, q.s2)
