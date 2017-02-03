from makePuzzles import *

def printPuzzle(puz):
	rows = len(puz)
	cols = len(puz[0])
	for i in range(0, rows):
		for j in range(0, cols):
			print(puz[i][j], end=" ")
		print("\n")

def complete(puz):
	rows = len(puz)
	cols = len(puz[0])
	for i in range(rows):
		counti = 0
		countj = 0
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

			count = numAdjacent(puz, i, j)
			#don't know how to convert the string to an int
			if puz[i][j] == "0" and count != 0:
					#print("Incorrect on a 0")
					return False
			if puz[i][j] == "1" and count != 1:
					#print("Incorrect on a 2")
					return False
			if puz[i][j] == "2" and count != 2:
					#print("Incorrect on a 2")
					return False
			if puz[i][j] == "3" and count != 3:
					#print("Incorrect on a 3")
					return False
			if puz[i][j] == "4" and count != 4:
					#print("Incorrect on a 4")
					return False
	retVal = True
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

def legal(puz):
	rows = len(puz)
	cols = len(puz[0])
	#print("==== Check legality")
	#printPuzzle(puz)
	for i in range(rows):
		counti = 0
		countj = 0
		for j in range(cols):
			if puz[i][j] == "b":
				counti += 1
				if counti > 1:
					#print("More than one in row")
					return False
			elif puz[i][j] != "_":
				counti = 0

			if puz[j][i] == "b":
				countj += 1
				if countj > 1:
					#print("More than one in column")
					return False
			elif puz[j][i] != "_":
				countj = 0

			count = numAdjacent(puz, i, j)
			#don't know how to convert the string to an int
			if puz[i][j] == "0" and count > 0:
					#print("Too many on a 0")
					return False
			if puz[i][j] == "1" and count > 1:
					#print("Too many on a 1")
					return False
			if puz[i][j] == "2" and count > 2:
					#print("Too many on a 2")
					return False
			if puz[i][j] == "3" and count > 3:
					#print("Too many on a 3")
					return False
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

def backtrack (puz, domain, notassigned):
	if complete(puz):
		return puz

	if len(notassigned)== 0:
		return "back"
	val = notassigned.pop()
	i = int(val/len(puz))
	j = int(val%len(puz))

	for value in domain:
		puz[i][j] = value
		if value != "_" and legal(puz) or value == "_":
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




if __name__ == '__main__':
    main()
