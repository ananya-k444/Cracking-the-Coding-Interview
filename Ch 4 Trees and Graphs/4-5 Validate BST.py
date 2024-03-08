class Node:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None


def inorder(root):
	if root is None:
		return

	inorder(root.left)
	print(root.val, end=' ')
	inorder(root.right)


def insertBST(root, val):
	node = Node(val)

	if root is None:
		root = Node(val)

	elif val <= root.val:
		root.left = insertBST(root.left, val)

	else:
		root.right = insertBST(root.right, val)

	return root


def findMax(root):
	if root is None:
		return 0

	leftMax = findMax(root.left)
	rightMax = findMax(root.right)

	value = 0
	if leftMax > rightMax:
		value = leftMax
	else:
		value = rightMax

	if value < root.val:
		value = root.val

	return value


def findMin(root):
	if root is None:
		return 1000000

	leftMin = findMin(root.left)
	rightMin = findMin(root.right)

	value = 0
	if leftMin < rightMin:
		value = leftMin
	else:
		value = rightMin

	if value > root.val:
		value = root.val

	return value


def isBST(root):
	if root is None:
		return True

	if root.left and findMax(root.left) > root.val:
		return False

	if root.right and findMin(root.right) < root.val:
		return False

	if (isBST(root.left) is False) or (isBST(root.right) is False):
		return False

	return True


# # first insert into tree1
# root = None
# vals = [5, 10, 7, 2, 1, 13, 3, 20]

# for val in vals:
# 	root = insertBST(root, val)
# 	print("Inorder traversal: ", end='')
# 	inorder(root)
# 	print()

# # check if the tree is BST
# if ifBST(root):
# 	print("The tree is a BST")
# else:
# 	print("The tree is NOT a BST")


# tree2
root2 = Node(5)
root2.left = Node(2)
root2.left.right = Node(6)
# root2.right = Node(4)
if ifBST(root2):
	print("The tree is a BST")
else:
	print("The tree is NOT a BST")
