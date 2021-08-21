import copy

#constants
MOVES = ["up", "down", "left", "right"]
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
INPUT_STATE = [[1, 8, 2], [0, 4, 3], [7, 6, 5]]

#node set when we get the result while searching
RESULT_NODE = None

#node class with members as current state and parent pointer
class Node:
    def __init__(self, parent, state):
        self.parent = parent
        self.state = state

    def isGoalNode(self):
        return GOAL_STATE == self.state

    def printNode(self):
        n = len(self.state)

        for i in range(n):
            print()
            for j in range(n):

                print(self.state[i][j], end="  ")

    #generate succesors of a node
    def getSuccesors(self):

        res = []
        for move in MOVES:
            if self.isValidMove(move):

                state = self.performMove(move)
                new_node = Node(self, state)
                res.append(new_node)

        return res

    #get position(i,j)mof blank tile(0)
    def getBlankTile(self):
        n = len(self.state)

        for i in range(n):
            for j in range(n):
                if self.state[i][j] == 0:

                    return i, j

    #check if a move is valid 
    def isValidMove(self, move):

        i, j = self.getBlankTile()
        n = len(self.state)

        if move == "up" and i != 0:

            return True

        if move == "down" and i != n - 1:

            return True

        if move == "left" and j != 0:

            return True

        if move == "right" and j != n - 1:

            return True

        return False

    #perform the given move
    def performMove(self, move):

        mat = self.state
        copy_mat = copy.deepcopy(mat)
        i, j = self.getBlankTile()

        if move == "up":
            copy_mat[i][j] = copy_mat[i - 1][j]
            copy_mat[i - 1][j] = 0

        elif move == "down":
            copy_mat[i][j] = copy_mat[i + 1][j]
            copy_mat[i + 1][j] = 0

        elif move == "left":
            copy_mat[i][j] = copy_mat[i][j - 1]
            copy_mat[i][j - 1] = 0

        elif move == "right":
            copy_mat[i][j] = copy_mat[i][j + 1]
            copy_mat[i][j + 1] = 0

        return copy_mat


#depth limited search
def depth_limited_search(srcNode, limit):

    #return if goal node found 
    if srcNode.isGoalNode():

        global RESULT_NODE
        RESULT_NODE = srcNode
        return True

    #cuttoff if limit exceeded
    if limit <= 0:

        return False

    #generate succesors
    succ = srcNode.getSuccesors()

    for s in succ:
        if depth_limited_search(s, limit - 1):
            return True

    return False

#IDDFS
def iterative_deepening(srcNode):

    for i in range(100):
        if depth_limited_search(srcNode, i):

            print(f"\nsolution found at depth {i}")
            return True

    print("MAX DEPTH LIMIT EXCEEDED")

#print the moves by backtraking using parent pointers
def getMoves():

    curr = RESULT_NODE
    SOLUTION_MOVES = []
    
    while curr is not None:
    
        SOLUTION_MOVES.append(curr)
        curr = curr.parent
    
    start_node = SOLUTION_MOVES.pop()
    prev_pos = start_node.getBlankTile()
    
    print("-----------------------INITIAL STATE------------------------")
    start_node.printNode()
    
    while len(SOLUTION_MOVES) != 0:
    
        curr = SOLUTION_MOVES.pop()
        curr_pos = curr.getBlankTile()
    
        print(f"\n\nmove blank from {prev_pos} to {curr_pos}")
    
        prev_pos = curr_pos
        curr.printNode()
    
    print("\n\n-----------------------FINAL STATE--------------------------")
    
srcNode = Node(None, INPUT_STATE)
iterative_deepening(srcNode)
getMoves()
