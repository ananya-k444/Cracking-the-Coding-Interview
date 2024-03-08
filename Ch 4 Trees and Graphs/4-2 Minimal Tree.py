class Node:
	def __init__(self, val):
		self.val = val
		self.right = self.left = None


def inOrder(root):
	if root is None:
		return

	inOrder(root.left)
	print(root.val, end=' ')
	inOrder(root.right)


def createMinimalTree(arr):
	if not arr:
		return None

	mid = len(arr) // 2
	root = Node(arr[mid])

	root.left = createMinimalTree(arr[:mid])
	root.right = createMinimalTree(arr[mid+1:])

	return root


sort_arr = [1, 2, 3, 5, 7, 10, 13, 20]
root = createMinimalTree(sort_arr)

print("Inorder traversal of tree: ")
inOrder(root)