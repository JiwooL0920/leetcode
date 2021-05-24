# in order
class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data

	def printTree(self):
		if self.left:
			self.left.printTree()
		print(self.data)
		if self.right:
			self.right.printTree()


	# left subttree is visiteted first, tthen the eroot and later the right subtree
	# rem: every node may represent a subtree itself
	def inorderTraversal(self, root):
		res = []
		if root:
			res = self.inorderTraversal(root.left)
			res.append(root.data)
			res = res + self.inorderTraversal(root.right)
		return res

	# root node is visited first, then the left subtree and right subtree
	def preorderTraversal(self, root):
		res = []
		if root:
			res.append(root.data)
			res = res + self.preorderTraversal(root.left)
			res = res + self.preorderTraversal(root.right)
		return res

	# left subtree -> right subtree -> root
	def postorderTraversal(self, root):
		res = []
		if root:
			res = self.postorderTraversal(root.left)
			res = res + self.postorderTraversal(root.right)
			res.append(root.data)
		return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inorderTraversal(root))
# print(root.preorderTraversal(root))
# print(root.postorderTraversal(root))
