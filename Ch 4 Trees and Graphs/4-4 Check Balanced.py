class Node:
	def __init__(self, val):
		self.val = val
		self.left = self.right = None


def inOrder(root):
	if root is None: 
		return

	inOrder(root.left)
	print(root.val, end=' ')
	inOrder(root.right)


def findHeight(root):
	if root is None:
		return 0

	h_left = findHeight(root.left)
	h_right = findHeight(root.right)

	return max(h_left, h_right) + 1


def checkBalanced(root):
	if root is None:
		return True

	if abs(findHeight(root.left) - findHeight(root.right)) > 1:
		return False

	return True


# balanced
root = Node(5)
root.left = Node(2)
root.left.right = Node(6)
# root.left.right.right = Node(7)
root.right = Node(4)

# unbalanced
root2 = Node(5)
root2.left = Node(2)
root2.left.right = Node(6)
root2.left.right.right = Node(7)
root2.right = Node(4)

# unbalanced
root3 = Node(1)
root3.right = Node(2)
root3.right.right = Node(3)
root3.right.right.right = Node(4)
root3.right.right.right.right = Node(5)

# unbalanced
root4 = Node(1)
root4.right = Node(2)
root4.left = Node(3)
root4.left.left = Node(4)
root4.left.right = Node(5)
root4.left.right.left = Node(6)
root4.left.right.left.left = Node(7)


if checkBalanced(root4):
	print("Tree is balanced")
else:
	print("Tree is NOT balanced")

