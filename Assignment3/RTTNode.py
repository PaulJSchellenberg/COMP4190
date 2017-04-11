import math
import sys

class RTTNode:
    def __init__(self,row,col,parent):
        self.parent = parent
        self.row=row
        self.col=col
        self.length=sys.maxsize

    def changeParent(self,parent):
        self.parent = parent
        if not parent == None:
            self.length = parent.length+parent.getDistance(self.row,self.col)
        else:
            self.length = sys.maxsize

    def getDistanceFromStart(self,row,col):
        distance = math.sqrt((row-self.row)**2+(col-self.col)**2)+ self.length
        return distance

    def getDistance(self,row,col):
        distance = math.sqrt((row-self.row)**2+(col-self.col)**2)
        return distance

    def getUnitVector(self,row,col):
        distance = self.getDistance(row,col)
        rowV = (row-self.row)/distance
        colV = (col-self.col)/distance
        return rowV,colV
