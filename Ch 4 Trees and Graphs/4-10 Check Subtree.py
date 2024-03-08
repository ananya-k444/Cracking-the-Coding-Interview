class Node:
	def __init__(self, val):
		self.val = val
		self.left = self.right = None


def containsTree(root1, root2):
	string1, string2 = [], []

	getOrder(root1, string1)
	getOrder(root2, string2)

	# print("string1: ", string1)
	# print("string2: ", string2)

	return (''.join(string2) in ''.join(string1))


def getOrder(root, preOrderStr):
	if root is None:
		preOrderStr.append('X')
		return

	preOrderStr.append(str(root.val))
	getOrder(root.left, preOrderStr)
	getOrder(root.right, preOrderStr)


root1 = Node(7)
root1.left = Node(2)
root1.right = Node(6)
root1.right.left = Node(11)
root1.right.left.right = Node(4)
root1.right.right = Node(13)

root2 = Node(6)
root2.left = Node(11)
root2.left.right = Node(4)
# root2.right = Node(13)

if containsTree(root1, root2):
	print("T2 is a subtree of T2")
else:
	print("T2 is NOT a subtree of T2")