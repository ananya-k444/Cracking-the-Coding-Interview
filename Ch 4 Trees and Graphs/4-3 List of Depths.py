# node for the tree
class Node:
	def __init__(self, val):
		self.val = val
		self.left = self.right = None


# node for the linked lists
class LLNode:
	def __init__(self, val):
		self.val = val
		self.next = None


# find height of the tree
def findHeight(root):
	if root is None:
		return 0

	left_h = findHeight(root.left)
	right_h = findHeight(root.right)

	return max(left_h, right_h) + 1


# visualise the tree
def inorder(root):
	if root is None:
		return 

	inorder(root.left)
	print(root.val, end=' ')
	inorder(root.right)


# our function of interest
def listOfDepths(root, height, hashmap):	# DFS
	hashmap[height-1].append(root.val)

	if root.left:
		listOfDepths(root.left, height-1, hashmap)
	if root.right:
		listOfDepths(root.right, height-1, hashmap)


root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)

print("Inorder traversal of tree: ")
inorder(root)
print("\n")

height = findHeight(root)
hashmap = [ [] for _ in range(height) ]
listOfDepths(root, height, hashmap)

for h in range(height):
	print("level elements: ", hashmap[h])