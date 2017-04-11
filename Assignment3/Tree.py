from RRTNode import *

class Tree:
    def __init__(self,start,end):
        self.start = RRTNode(start[0],start[1],None)
        self.end = RRTNode(end[0],end[1],None)
        self.Nodes = []
        self.Nodes.append(self.start)
