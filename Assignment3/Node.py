from QuadTree import *
import math

class Node:
	def __init__(self, leaf, end):
		self.leaf = leaf
		self.G = 100000
		self.H = self.distance(end)
		self.parent = None
		
	def distance(self, other):
		return math.sqrt((self.leaf.centerx - other.centerx)**2 + (self.leaf.centery - other.centery)**2)