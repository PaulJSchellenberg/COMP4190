import random

class Domain:
    def __init__(self,size):
        self.start=(0,0)
        self.end=(0,0)
        self.size = size
        self.grid = [[' ' for x in range(size)] for y in range(size)]
        self.num=-1
        self.nums=[]
        self.allPos = []

    def fillDomain(self,obs):
        for ob in range(obs):
            centerpos = (random.randint(0,self.size),random.randint(0,self.size))
            size = (random.randint(10,50),random.randint(10,50))
            halves = [int(x/2.) for x in size]

            #bounds format: [top,bottom,left,right]
            bounds = [max(0,centerpos[0]-halves[0]),
                        min(self.size,centerpos[0]+size[0]-halves[0]),
                        max(0,centerpos[1]-halves[1]),
                        min(self.size,centerpos[1]+size[1]-halves[1])]

            for i in range(bounds[0],bounds[1]):
                for j in range(bounds[2],bounds[3]):
                    self.grid[i][j]='#'

        self.placeStartAndEnd()

        for i in range(self.size):
            for j in range(self.size):
                self.fillPos((i,j),'#')

    def placeStartAndEnd(self):
        for i in range(self.size):
            for j in range(self.size):
                self.fillPos((i,j),' ')

        self.start = (random.randint(0,self.size-1),random.randint(0,self.size-1))
        while self.grid[self.start[0]][self.start[1]] == '#':
            self.start = (random.randint(0,self.size-1),random.randint(0,self.size-1))

        numstart = self.grid[self.start[0]][self.start[1]]

        self.grid[self.start[0]][self.start[1]] = 'S'



        self.end = (random.randint(0,self.size-1),random.randint(0,self.size-1))
        while not(self.grid[self.end[0]][self.end[1]] == numstart):
            self.end = (random.randint(0,self.size-1),random.randint(0,self.size-1))

        self.grid[self.end[0]][self.end[1]] = 'E'



        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == numstart:
                    self.allPos.append((i,j))
                if self.grid[i][j] in self.nums:
                    self.grid[i][j]=' '

        self.num=-1
        self.nums=[]


    def fillPos(self,pos,char):
        stop = False
        vertToVisit = [(pos[0],pos[1])]
        while len(vertToVisit) >0:
            vert = vertToVisit.pop()
            if self.grid[vert[0]][vert[1]] == char:
                neighbors = self.getNeighbors((vert[0],vert[1]))
                found = False
                for neighbor in neighbors:
                    if self.grid[neighbor[0]][neighbor[1]] in self.nums:
                        found=True
                    if self.grid[neighbor[0]][neighbor[1]] == char:
                        vertToVisit.append((neighbor[0],neighbor[1]))

                if not found:
                    self.num+=1
                    self.nums.append(str(self.num))

                self.grid[vert[0]][vert[1]]=str(self.num)



    def getNeighbors(self,pos):
        neighbors = []
        if pos[0]+1<self.size:
            neighbors.append((pos[0]+1,pos[1]))
        if pos[1]-1>=0:
            neighbors.append((pos[0],pos[1]-1))
        if pos[1]+1<self.size:
            neighbors.append((pos[0],pos[1]+1))
        if pos[0]-1>=0:
            neighbors.append((pos[0]-1,pos[1]))
        return neighbors


    def printDomain(self):
        border = self.size+2
        ret=''
        for i in range(-1,self.size+1):
            for j in range(-1,self.size+1):
                if (i==-1 or i==self.size) and (j==-1 or j==self.size):
                    ret+='+'
                elif i==-1 or i==self.size:
                    ret+='-'
                elif j==-1 or j==self.size:
                    ret+='|'
                else:
                    ret+=str(self.grid[i][j])
            ret+='\n'
        print(ret)
