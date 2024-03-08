class Node:
	def __init__(self, val):
		self.val = val
		self.right = self.left = None


def containsTree(r1, r2):
	if r2 is None:
		return True

	return subTree(r1, r2)


def subTree(r1, r2):
	if r1 is None:
		return False
	elif (r1.val == r2.val) and matchTrees(r1, r2):
		return True

	return subTree(r1.left, r2) or subTree(r1.right, r2)


def matchTrees(r1, r2):
	if (r1 is None) and (r2 is None):
		return True
	elif (r1 is None) or (r2 is None):
		return False
	elif r1.val and r2.val:
		return False
	else:
		return matchTrees(r1.left, r2.left) and matchTrees(r1.right, r2.right)
		

root1 = Node(7)
root1.left = Node(2)
root1.right = Node(6)
root1.right.left = Node(11)
root1.right.left.right = Node(4)
root1.right.right = Node(13)

root2 = Node(6)
root2.left = Node(11)
root2.left.right = Node(4)
root2.right = Node(13)

if containsTree(root1, root2):
	print("T2 is a subtree of T2")
else:
	print("T2 is NOT a subtree of T2")