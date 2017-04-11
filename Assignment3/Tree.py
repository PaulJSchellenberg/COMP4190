from RTTNode import *

class Tree:
    def __init__(self,start,end):
        self.start = RTTNode(start[0],start[1],None)
        self.end = RTTNode(end[0],end[1],None)
        self.Nodes = []
        self.Nodes.append(self.start)
