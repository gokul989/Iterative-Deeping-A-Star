import heapq
import math
import copy
import sys
import time

#node class for representing Node
class Node:
    def __init__(self, state, gval, hval, directionstr,lastDir):
        self.state = state        
        self.gval = gval 
        self.hval = hval
        self.dir = directionstr
        self.lastdir = lastDir
    def __lt__(self,other):
	    return (self.gval+self.hval) < (other.gval+self.hval)

# returns manhattan heuristic value
def manhattan(state,N):
	x = 0;
	for i in range(N):
		for j in range(N):
			if(state[i][j] == 0):
				continue
			y= abs(i - math.floor((state[i][j]-1)/N)) + abs(j - (state[i][j]-1)%N)			
			x += y			
	return x;	

# returns number of tiles out of place as heuristic value
def TilesOutofPlace(state,N):
	x = 0;
	count = 1;
	for i in range(N):
		for j in range(N):
			if(state[i][j] != 0 and state[i][j] != count):
				x += 1
			count +=1
	
	return x;

# flag = 1 selects manhattan distance as heuristic. otherwise Tiles out of place.Default is manhattan
def heuristic(state,N):
		flag = 1
		if(flag == 1):
			return manhattan(state,N)
		return TilesOutofPlace(state,N)

#finds the position of zero in current state
def findZero(node):	
	for i in range(N):
		for j in range(N):
			if(node[i][j] == 0):
				return (i,j);
	return 0,0	

#generates valid children of a given node of NxN array size. Also avoids generating the parent node of current node as a child
def genChildren(node,N):
	nn1 = [];
	x,y = findZero(node.state);
	validDir = [1,1,1,1] # L U R D directions
	if(node.lastdir == "R"):
		validDir[0] = 0
	if(node.lastdir == "L"):
		validDir[2] = 0
	if(node.lastdir == "U"):
		validDir[3] = 0
	if(node.lastdir == "D"):
		validDir[1] = 0
		
	if(x == 0):
		validDir[1] = 0;
	if(y == 0):
		validDir[0] = 0;
	if(y == N-1):
		validDir[2] = 0;
	if(x == N-1):
		validDir[3] = 0;
	
	tempstate1 = copy.deepcopy(node.state);
	tempstate2 = copy.deepcopy(node.state);
	tempstate3 = copy.deepcopy(node.state);
	tempstate4 = copy.deepcopy(node.state);
	if(validDir[0] == 1):
		tempstate1[x][y],tempstate1[x][y-1] = tempstate1[x][y-1],tempstate1[x][y]
		nn2 = Node(tempstate1,node.gval+1,heuristic(tempstate1,N),node.dir +",L","L")
		nn1.append(nn2)
	if(validDir[1] == 1):
		tempstate2[x][y],tempstate2[x-1][y] = tempstate2[x-1][y],tempstate2[x][y]
		nn2 = Node(tempstate2,node.gval+1,heuristic(tempstate2,N),node.dir +",U","U")
		nn1.append(nn2)
	if(validDir[2] == 1):
		tempstate3[x][y],tempstate3[x][y+1] = tempstate3[x][y+1],tempstate3[x][y]		
		nn2 = Node(tempstate3,node.gval+1,heuristic(tempstate3,N),node.dir +",R","R")		
		nn1.append(nn2)
		
	if(validDir[3] == 1):
		tempstate4[x][y],tempstate4[x+1][y] = tempstate4[x+1][y],tempstate4[x][y]		
		nn2 = Node(tempstate4,node.gval+1,heuristic(tempstate4,N),node.dir +",D","D")
		nn1.append(nn2)
	return nn1;

# A* algorithm 
def AStar(node,N):
	start = time.time()
	openList = []
	closedList = {}
	openDict = {}
	openList.append((node.hval+node.gval, node))	
	openDict[str(node.state)] = node.hval+node.gval
	while len(openList) > 0:		
		tempf,tempNode = heapq.heappop(openList)
		if(tempNode.state == goal):
			end = time.time();
			print("Goal state reached :",tempNode.state)
			print(tempNode.dir[1:])			
			print(end-start,"s")			
			print("depth ",tempNode.gval)
			print("number of states visited ",len(closedList))			
			return tempNode.dir[1:]
		closedList[str(tempNode.state)] = tempNode 
		children = genChildren(tempNode,N)
		for i in range(len(children)):
			tempNode = children[i]
			if not (str(tempNode.state) in closedList or (str(tempNode.state) in openDict and (openDict[str(tempNode.state)])< (tempNode.hval + tempNode.gval))):
				heapq.heappush(openList, (tempNode.hval+tempNode.gval, tempNode))
				openDict[str(tempNode.state)] = tempNode.hval+ tempNode.gval	
	return "";

#IDA* algorithm
def IDAStar(node,gg,t,N):
	hh = node.hval
	if(hh == 0):
		return True,node,0
	ff = gg + hh
	if(ff > t):
		return False,node,ff
	children = genChildren(node,N)
	min = 99999;
	for i in range(len(children)):
		found,tNode,temp = IDAStar(children[i],gg+1,t,N)
		if(found == True):
			return True,tNode,0
		if(temp<min):
			min = temp
	return False,node,min

# 'main' section - takes the command line args and drives the program further.
if __name__ == '__main__':
	flag = int(sys.argv[1]) # flag = 1 for A* , 2 for IDA*
	N = int(sys.argv[2])  # N = 3 for 8-puzzle N = 4 for 15-puzzle
	filepath = sys.argv[3] #input file path
	outputpath = sys.argv[4] #output file path
	
	text_file = open(outputpath, "w")
	

	if N == 4:		
		goal = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
		input = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	if(N == 3):
		goal = [[1,2,3],[4,5,6],[7,8,0]]
		input = [[0,0,0],[0,0,0],[0,0,0]]

	fp = open(filepath,'r')
	data = fp.readlines()
	j=0
	for line in data:
		words = line.split(",")	
		for i in range(len(words)):			
			if(words[i]== ''):
				words[i] = 0
			try:
				input[j][i] = int(words[i])
			except:
				input[j][i] = 0;	
		j = j+1

	print("input state is",input)
	nn = Node(input,0,heuristic(input,N),"","")
	if(flag == 1):
		s = AStar(nn,N)		
	elif(flag==2):
		start = time.time()
		bound =  nn.hval
		found = False
		while(not found):
			#print("bound ---",bound)
			found,goalNode,t = IDAStar(nn,0,bound,N)
			if(found == False):
				bound = t;				
		end = time.time()
		print(end-start,"s")
		print("Goal state reached: ",goalNode.state)
		print("depth ",goalNode.gval)
		print(goalNode.dir[1:])
		s = goalNode.dir[1:]
	text_file.write(s)
	text_file.close()