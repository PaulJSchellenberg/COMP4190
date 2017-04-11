import sys
from Domain import *
from QuadTree import *
from Graph import *
from Node import *
import random
from queue import PriorityQueue
import math
from RRT import *
import copy
import time


def quadtree(bigfloor):
	tree = QuadTree(None, 0, len(bigfloor.grid[0]), 0, len(bigfloor.grid))
	quadtreesub(bigfloor.grid, tree)
	return tree

def quadtreesub(bigfloor, tree):
	count = 0
	for x in range(tree.x1, tree.x2):
		for y in range(tree.y1, tree.y2):
			if bigfloor[x][y] == 'S':
				tree.hasStart = True
			elif bigfloor[x][y] == 'E':
				tree.hasEnd = True
			elif bigfloor[x][y] != ' ':
				count += 1

	if tree.x2 - tree.x1 == 0 or tree.y2 - tree.y1 == 0:
		return False
	elif count == (tree.x2-tree.x1)*(tree.y2-tree.y1):
		return False

	elif count == 0:
		return True

	else:
		sub = []
		sub.append(QuadTree(tree, tree.x1, (tree.x1+tree.x2)//2, tree.y1, (tree.y1+tree.y2)//2))
		sub.append(QuadTree(tree, (tree.x1+tree.x2)//2, tree.x2, tree.y1, (tree.y1+tree.y2)//2))
		sub.append(QuadTree(tree, tree.x1, (tree.x1+tree.x2)//2, (tree.y1+tree.y2)//2, tree.y2))
		sub.append(QuadTree(tree, (tree.x1+tree.x2)//2, tree.x2, (tree.y1+tree.y2)//2, tree.y2))

		for i in range(4):
			if quadtreesub(bigfloor, sub[i]):
				tree.children.append(sub[i])
		return True

def drawLine(grid, x1, x2, y1, y2):
	if x2 - x1 != 0:
		slope = (y2-y1)/(x2-x1)
		if x1 < x2:
			for x in range(x1,x2):
				if grid[x][int(y1 + slope * (x-x1))] == ' ':
					grid[x][int(y1 + slope * (x-x1))] = 'x'
		else:
			for x in range(x2,x1):
				if grid[x][int(y1 + slope * (x-x1))] == ' ':
					grid[x][int(y1 + slope * (x-x1))] = 'x'
	if y2 - y1 != 0:
		slope = (x2-x1)/(y2-y1)
		if y1 < y2:
			for y in range(y1,y2):
				if grid[int(x1 + slope * (y-y1))][y] == ' ':
					grid[int(x1 + slope * (y-y1))][y] = 'x'
		else:
			for y in range(y2,y1):
				if grid[int(x1 + slope * (y-y1))][y] == ' ':
					grid[int(x1 + slope * (y-y1))][y] = 'x'

def findChar(grid, leaf, ch):
	for x in range(leaf.x1, leaf.x2):
		for y in range(leaf.y1, leaf.y2):
			if grid[x][y] == ch:
				return (x,y)

def main():
	obNum = int(sys.argv[1])
	size = int(sys.argv[2])

	if size%2 != 0:
		print("Enter an even size")
	else:
		floorPlan = Domain(size)
		floorPlan.fillDomain(obNum)
		#floorPlan.printDomain()

		RRTMap = copy.deepcopy(floorPlan)

		start = time.time()
		tree = quadtree(floorPlan)
		graph = Graph(tree)
		path = graph.aStar()
		end= time.time()
		for i in range(1,len(path)):
			drawLine(floorPlan.grid, path[i-1].centerx, path[i].centerx, path[i-1].centery, path[i].centery)
		(startx, starty) = findChar(floorPlan.grid, graph.start.leaf, 'S')
		(endx, endy) = findChar(floorPlan.grid, graph.end.leaf, 'E')
		drawLine(floorPlan.grid, path[0].centerx, endx, path[0].centery, endy)
		drawLine(floorPlan.grid, path[-1].centerx, startx, path[-1].centery, starty)
		tree.printTree(floorPlan.grid)
		print('Time for QuadTree: {0}\n'.format(end-start))

		RRTtime,RRTlength = RRT(RRTMap)
		print('Time for RRT: {0}'.format(RRTtime))
		print('Distance for RRT: {0}'.format(RRTlength))


if __name__ == '__main__':
	main()
