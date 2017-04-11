from RRTNode import *
from Tree import *
from Domain import *
import random
import time

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

def countNeighbors(row,col,tree):
    count=0
    for node in tree.Nodes:
        if abs(row-node.row)<6 and abs(col-node.col)<6:
            count+=1
    return count

def getRand(domain,tree):
    rows = len(domain.grid)
    cols = len(domain.grid[0])

    randRow = random.randint(0,rows-1)
    randCol = random.randint(0,cols-1)

    distanceToEnd = math.sqrt((domain.end[0]-randRow)**2+(domain.end[1]-randCol)**2)

    randTake = random.random()**2

    neighbors = countNeighbors(randRow,randCol,tree)

    take = 1.3**-(2*((neighbors/2+1)**0.6)*distanceToEnd**1.7/domain.size)


    while domain.grid[randRow][randCol] !=' ' and randTake>take:

        randRow = random.randint(0,rows-1)
        randCol = random.randint(0,cols-1)

        distanceToEnd = math.sqrt((domain.end[0]-randRow)**2+(domain.end[1]-randCol)**2)

        randTake = random.random()**2

        neighbors = countNeighbors(randRow,randCol,tree)

        take = 1.3**-(2*((neighbors/2+1)**0.6)*distanceToEnd**1.7/domain.size)
        #print(randTake,take)


    return RRTNode(randRow,randCol,None)

def getStep(domain,fromNode,toNode):
    # return None if there is an obstacle between toNode and fromNode
    # return toNode if toNode is within 20 units
    # return a step length 20 units in the direction of toNode
    ret = toNode

    distance = fromNode.getDistance(toNode.row,toNode.col)
    stepSize = 20
    if distance<stepSize:
        stepSize=distance

    if stepSize!=0:
        rowV,colV = fromNode.getUnitVector(toNode.row,toNode.col)

        for i in range(int(stepSize*1.2)):
            ite = i*stepSize/int(stepSize*1.2)
            row = fromNode.row+int(rowV*ite)
            col = fromNode.col+int(colV*ite)
            if domain.grid[row][col]==' ' or domain.grid[row][col]=='E' or domain.grid[row][col]=='S':
                ret = RRTNode(row,col,None)
            else:
                ret = None
                break;
    return ret


def checkComplete(domain,tree):
    ret = True
    distance = tree.Nodes[-1].getDistance(tree.end.row,tree.end.col)
    stepSize=20
    if distance<=stepSize:
        stepSize=distance
        rowV,colV = tree.Nodes[-1].getUnitVector(tree.end.row,tree.end.col)
        for i in range(int(stepSize*1.2)):
            ite = i*stepSize/int(stepSize*1.2)
            row = tree.Nodes[-1].row+int(rowV*ite)
            col = tree.Nodes[-1].col+int(colV*ite)
            if not(domain.grid[row][col]==' ' or domain.grid[row][col]=='E' or domain.grid[row][col]=='S'):
                ret = False
                break;
        if ret:
            tree.end.changeParent(tree.Nodes[-1])
    else:
        ret=False
    return ret

def trace(tree):
    Nodes = []
    Node = tree.end
    while Node != None:
        Nodes.append(Node)
        Node = Node.parent

    return Nodes

def RRT(domain):
    start = time.time()
    tree = Tree(domain.start,domain.end)
    tree.start.length=0
    complete = checkComplete(domain,tree)
    count = 0
    while not complete:
        randNode = getRand(domain,tree)
        closestDist = sys.maxsize
        closestNode = None
        disputes = []
        for node in tree.Nodes:
            dist = node.getDistance(randNode.row,randNode.col)
            if dist<20:
                disputes.append(node)
            if dist<closestDist:
                closestDist = dist
                closestNode = node
        if len(disputes)>1:
            closestDist = sys.maxsize
            for node in disputes:
                dist = node.getDistanceFromStart(randNode.row,randNode.col)
                if dist<closestDist:
                    closestDist = dist
                    closestNode = node


        step = getStep(domain,closestNode,randNode)
        if step!=None:
            step.changeParent(closestNode)
            tree.Nodes.append(step)
            count+=1
            #print('{0}\r'.format(len(tree.Nodes)))


        complete = checkComplete(domain,tree)
        #complete = True

    end = time.time()

    path = trace(tree)
    prev = path.pop()

    for i  in range(1,len(path)+1):
        node = path.pop()
        drawLine(domain.grid,prev.row,node.row,prev.col,node.col)
        prev=node

    print('RRT')
    domain.printDomain()
    return end-start,tree.end.length

























#
