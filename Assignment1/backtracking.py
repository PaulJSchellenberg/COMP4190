from makePuzzles import *

wallNums = ['0','1','2','3','4']

def checkEdgeCorner(puz,i,j):
    # not an edge or corner status = 0
    # an edge, status = 1
    # a corner status = 2
    status = 0
    if(i==0 or i==len(puz)-1):
        status+=1
    if(j==0 or j==len(puz[0])-1):
        status+=1

    return status

def countWalls(puz,i,j):
	#counts the number of walls adjacent to a cell
	#count increases 1 for walls 0-2.
	#Increases 2 for walls 3-4
	count = 0;
	if i>0 and puz[i-1][j] in wallNums:
		count+=int(int(puz[i-1][j])/2+1)
	if i<len(puz)-1 and puz[i+1][j] in wallNums:
		count+=int(int(puz[i+1][j])/2)+1
	if j>0 and puz[i][j-1] in wallNums:
		count+=int(int(puz[i][j-1])/2)+1
	if j<len(puz[0])-1 and puz[i][j+1] in wallNums:
		count+=int(int(puz[i][j+1])/2)+1
	return count

def checkAdjBeams(puz,i,j):
	# counts the number of beams that are adjacent to the point
	count = 0;
	if i>0 and puz[i-1][j]=='+':
		count+=1
	if i<len(puz)-1 and puz[i+1][j]=='+':
		count+=1
	if j>0 and puz[i][j-1]=='+':
		count+=1
	if j<len(puz[0])-1 and puz[i][j+1]=='+':
		count+=1
	return count

def findConstraining(puz,notassigned):
	print('underconstruction')
	quit()

def findConstrained(puz,notassigned):
	rows = len(puz)
	cols = len(puz[0])
	winner = (-1,-1)

	# marks the rays
	for i in range(rows):
		for j in range(cols):


			#"raytrace" away from bulbs, setting all _ to + in a line in every direction
			if puz[i][j] == "b":
				k = 1
				while i + k < rows and (puz[i + k][j] == "_" or puz[i + k][j] == "+"):
					puz[i + k][j] = "+"
					k += 1
				k = 1
				while i - k >= 0 and (puz[i - k][j] == "_" or puz[i - k][j] == "+"):
					puz[i - k][j] = "+"
					k += 1
				k = 1
				while j + k < cols and (puz[i][j + k] == "_" or puz[i][j + k] == "+"):
					puz[i][j + k] = "+"
					k += 1
				k = 1
				while j - k >= 0 and (puz[i][j - k] == "_" or puz[i][j - k] == "+"):
					puz[i][j - k] = "+"
					k += 1
				k = 1

	# for each unassigned, check the contrained priority
	for val in notassigned:
		i = int(val/rows)
		j = int(val%rows)

		# check to see how many adjacent walls
		walls = countWalls(puz,i,j)
		# check to see if the cell is an edge, corner or neither
		loc = checkEdgeCorner(puz,i,j)
		# check to see how many beams are around the cell
		adjBeams = checkAdjBeams(puz,i,j)

		#add all these constraints up
		curr = walls+loc+adjBeams

		#if the value is the same as the current leader, randomly pick which to keep
		if curr==winner[0] and random.randint(0,1) == 0:
				winner = (curr,val)
		if curr > winner[0]:
			winner=(curr,val)

	#revert all '+' to '_'
	for i in range(rows):
		for j in range(cols):
			if puz[i][j] == "+":
				puz[i][j] = "_"

	return winner[1]




def getFromHeuristic(puz,notassigned,type):
	if type == 'random':
	    index = random.randint(0,len(notassigned)-1)
	    ret = notassigned[index]
	    notassigned.remove(ret)

	if type == 'constrained':
		ret = findConstrained(puz,notassigned)
		notassigned.remove(ret)

	if type == 'contraining':
		ret = findConstraining(puz,notassigned)
		notassigned.remove(ret)

	return ret

def printPuzzle(puz):
	rows = len(puz)
	cols = len(puz[0])
	for i in range(0, rows):
		for j in range(0, cols):
			print(puz[i][j], end=" ")
		print("\n")

def complete(puz):
	global wallNums
	rows = len(puz)
	cols = len(puz[0])
	retVal = True
	for i in range(rows):
		for j in range(cols):
			if puz[i][j] in wallNums and int(puz[i][j])!=numAdjacent(puz,i,j):
				return False

	for i in range(rows):
		for j in range(cols):


			#"raytrace" away from bulbs, setting all _ to + in a line in every direction
			if puz[i][j] == "b":
				k = 1
				while i + k < rows and (puz[i + k][j] == "_" or puz[i + k][j] == "+"):
					puz[i + k][j] = "+"
					k += 1
				k = 1
				while i - k >= 0 and (puz[i - k][j] == "_" or puz[i - k][j] == "+"):
					puz[i - k][j] = "+"
					k += 1
				k = 1
				while j + k < cols and (puz[i][j + k] == "_" or puz[i][j + k] == "+"):
					puz[i][j + k] = "+"
					k += 1
				k = 1
				while j - k >= 0 and (puz[i][j - k] == "_" or puz[i][j - k] == "+"):
					puz[i][j - k] = "+"
					k += 1
				k = 1


	#print("==== Check completeness")
	#printPuzzle(puz)
	for i in range(rows):
		for j in range(cols):
			if puz[i][j] == "_":
				retVal = False
			elif puz[i][j] == "+":
				puz[i][j] = "_"
	#if retVal == False:
		#print("Not all lit")
	return retVal

def numAdjacent(puz, i, j):
	rows = len(puz)
	cols = len(puz[0])
	count = 0
	if i > 0 and puz[i-1][j] == "b":
		count += 1
	if i < rows-1 and puz[i+1][j] == "b":
		count += 1
	if j > 0 and puz[i][j-1] == "b":
		count += 1
	if j < cols-1 and puz[i][j+1] == "b":
		count += 1
	return count

def legal(puz,i,j):
	rows = len(puz)
	cols = len(puz[0])
	#print("==== Check legality")
	#printPuzzle(puz)
	k=i-1
	if k>=0 and puz[k][j] in wallNums:
		if numAdjacent(puz,k,j) > int(puz[k][j]):
			return False
	while k>=0 and not puz[k][j] in wallNums:
		if puz[k][j] == 'b':
			return False
		k-=1

	k=i+1
	if k<rows and puz[k][j] in wallNums:
		if numAdjacent(puz,k,j) > int(puz[k][j]):
			return False
	while k<rows and not puz[k][j] in wallNums:
		if puz[k][j] == 'b':
			return False
		k+=1

	k=j-1
	if k>=0 and puz[i][k] in wallNums:
		if numAdjacent(puz,i,k) > int(puz[i][k]):
			return False
	while k>=0 and not puz[i][k] in wallNums:
		if puz[i][k] == 'b':
			return False
		k-=1

	k=j+1
	if k<cols and puz[i][k] in wallNums:
		if numAdjacent(puz,i,k) > int(puz[i][k]):
			return False
	while k<cols and not puz[i][k] in wallNums:
		if puz[i][k] == 'b':
			return False
		k+=1
	return True

def getBlanks(puz):
	retVal = []
	for i in range(0,len(puz)*len(puz[0])):
		k = int(i/len(puz))
		j = int(i%len(puz[0]))
		if puz[k][j] == "_":
			retVal.append(i)
	return retVal

def solve(puz):
	domain = ("b", "_")
	notassigned = getBlanks(puz)
	return backtrack(puz, domain, notassigned)

countNodes=0
def backtrack (puz, domain, notassigned):
	if complete(puz):
		return puz
	global countNodes
	countNodes+=1
	if countNodes%10000 == 0:
		print(countNodes,end='\r')

	if len(notassigned)== 0:
		return "back"
	val = getFromHeuristic(puz,notassigned,'constrained')
	i = int(val/len(puz))
	j = int(val%len(puz))

	for value in domain:
		puz[i][j] = value
		if (value != "_" and legal(puz,i,j)) or value == "_":
			result = backtrack(puz, domain, notassigned)
			if result != "back":
				return result


	notassigned.append(val)
	return "back"

def clearSolution(puzzle):
	rows = len(puzzle)
	cols = len(puzzle[0])
	for i in range(rows):
		for j in range(cols):
			if puzzle[i][j] == 'b':
				puzzle[i][j] = '_'

def main( argv = None ):
    if (argv == None ):
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser(description='create a modified Akari Puzzle')
    parser.add_argument('--width', action='store', dest='width', type=int, default=8)
    parser.add_argument('--height', action='store', dest='height', type=int, default=8)
    parser.add_argument('--verbose', '-v', action='count', dest='verbose', default=0)
    parser.add_argument('--count', '-c', action='store', dest='count', default=1)
    parser.add_argument('--solution', '-s', action='store_true', dest='solution', default=False)
    parser.add_argument('--bulbs', '-b', action='store', dest='bulbs', type=int, default=-1)
    parser.add_argument('--walls', '-w', action='store', dest='walls', type=int, default=-1)

    args = parser.parse_args( argv )
    if (args.verbose > 0 ):
        print('AkariMaker {0}x{1} bulbs {2} walls {3}'.format(args.width, args.height, args.bulbs, args.walls ))

    puzzle = makePuzzles(args.count, args.width, args.height, args.bulbs, args.walls, args.solution )

    clearSolution(puzzle)

    print()

    printPuzzle(solve(puzzle))

    print(countNodes)




if __name__ == '__main__':
    main()
