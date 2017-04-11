from QuadTree import *
from Node import *

class Graph:
	def __init__(self, tree):
		self.start = None
		endLeaf = tree.getEnd(tree)
		startLeaf = tree.getStart(tree)
		self.end = Node(endLeaf, endLeaf)
		self.start = Node(startLeaf, endLeaf)
		self.nodes = []
		self.generateGraph(tree)
		
	def generateGraph(self, current):
		for child in current.children:
			if len(child.children) == 0:
				self.nodes.append(Node(child,self.end.leaf))
			else:
				self.generateGraph(child)
	
	def minDistance(self, nodes):
		minCost = 1000000
		min = nodes[0]
		for n in nodes:
			if n.G + n.H < min.G + min.H:
				min = n
				minCost = n.G + n.H
		return min
	
	def aStar(self):
		#The open and closed sets
		openset = []
		closedset = []
		#Current point is the starting point
		current = self.start
		#Add the starting point to the open set
		openset.append(current)
		#While the open set is not empty
		while len(openset) > 0:
			current = self.minDistance(openset)
			#If it is the item we want, retrace the path and return it
			if current.distance(self.end.leaf) == 0:
				path = []
				while current.parent:
					path.append(current.leaf)
					current = current.parent
				path.append(current.leaf)
				return path
			
			#Remove the item from the open set
			openset.remove(current)
			#Add it to the closed set
			closedset.append(current)
			#Loop through the node's children/siblings
			for node in self.getNeighbors(current):
				#If it is already in the closed set, skip it
				if node in closedset:
					continue
				#Otherwise if it is already in the open set
				if node in openset:
					#Check if we beat the G score 
					new_g = current.G + current.distance(node.leaf)
					if node.G > new_g:
					#If so, update the node to have a new parent
						node.G = new_g
						node.parent = current
				else:
					#If it isn't in the open set, calculate the G and H score for the node
					node.G = current.G + current.distance(node.leaf)
					node.H = current.distance(self.end.leaf)
					#Set the parent to our current item
					node.parent = current
					#Add it to the set
					openset.append(node)
					#Throw an exception if there is no path
		raise ValueError('No Path Found')
	
	def getNeighbors(self, this):
		ns = []
		for other in self.nodes:
			if (other.leaf.x1 == this.leaf.x2 or other.leaf.x2 == this.leaf.x1):
				if (other.leaf.y1 >= this.leaf.y1 and other.leaf.y2 <= this.leaf.y2):
					ns.append(other)
				elif (this.leaf.y1 >= other.leaf.y1 and this.leaf.y2 <= other.leaf.y2):
					ns.append(other)
			elif (other.leaf.y1 == this.leaf.y2 or other.leaf.y2 == this.leaf.y1):
				if (other.leaf.x1 >= this.leaf.x1 and other.leaf.x2 <= this.leaf.x2):
					ns.append(other)
				elif (this.leaf.x1 >= other.leaf.x1 and this.leaf.x2 <= other.leaf.x2):
					ns.append(other)
		return ns