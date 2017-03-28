import sys
from Domain import *



def main():
    obNum = int(sys.argv[1])
    size = int(sys.argv[2])

    floorPlan = Domain(size)
    floorPlan.fillDomain(obNum)
    floorPlan.printDomain()

if __name__ == '__main__':
    main()
