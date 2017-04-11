
class QuadTree:
	def __init__(self, parent, x1, x2, y1, y2):
		self.children = []
		self.parent = parent
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.hasStart = False
		self.hasEnd= False
		self.centerx = (x1 + x2)//2
		self.centery = (y1 + y2)//2
	
	def siblings(self):
		if parent != None:
			sibs = []
			for c in self.parent.children:
				if c != self:
					sibs.append(c)
			return sibs
		else:
			return None
		
	def neighbors(self, current, ns):
		if len(current.children) == 0 and current != self:
			#print ("\n=====\n(%d,%d),(%d,%d)" % (current.x1,current.y1,current.x2,current.y2))
			#print ("(%d,%d),(%d,%d)" % (self.x1,self.y1,self.x2,self.y2))
			if ((current.x1 == self.x2 or current.x2 == self.x1) and current.y1 >= self.y1 and current.y2 <= self.y2):
				ns.append(current)
			elif ((current.y1 == self.y2 or current.y2 == self.y1) and current.x1 >= self.x1 and current.x2 <= self.x2):
				ns.append(current)
		elif current != self:
			for c in current.children:
				self.neighbors(c, ns)
				
	def findNeighbors(self):
		current = self
		while current.parent != None:
			current = current.parent
		
		ns = []
		self.neighbors(current, ns)
		return ns
		
	def getStart(self, current):
		for child in current.children:
			if child.hasStart:
				if len(child.children) == 0:
					return child
				else:
					return child.getStart(child)
	
	def getEnd(self, current):
		for child in current.children:
			if child.hasEnd:
				if len(child.children) == 0:
					return child
				else:
					return child.getEnd(child)
					
	def printTree(self, grid):
		tree = self
		print ("(%d,%d),(%d,%d)" % (tree.x1,tree.y1,tree.x2,tree.y2))
		ret= "+"
		for i in range(tree.x1, tree.x2):
			ret += "-"
		ret += "+\n"
		for j in range(tree.y1, tree.y2):
			ret += "|"
			for i in range(tree.x1, tree.x2):
				ret+=str(grid[i][j])
			ret+="|\n"
			
		ret+="+"
		for i in range(tree.x1, tree.x2):
			ret += "-"
		ret += "+"
		
		print(ret + "\n")