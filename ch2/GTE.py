
# TreeNode class
class TreeNode():
	def __init__(self, children=[], value=None):
		self.children = children
		self.value = value

	def isLeaf(self):
		return not self.children

	def getValue(self):
		return self.value

	def getChildren(self):
		return self.children

# Game tree class 
class GTE():
	def __init__(self, root = None):
		self.root = root

	def evaluate(self, root, level=0):
		if self.root.isLeaf():
			return root.getValue()
		# even level 
		children = root.getChildren()
		childValues = [self.evaluate(child, level+1) for child in children]
		ret = None
		# take the max of children on even level
		if (level % 2 == 0):
			ret = max(childValues)
		# take the min of children on an odd level 
		else:
			ret = min(childValues)
		# return the value 
		return ret 




