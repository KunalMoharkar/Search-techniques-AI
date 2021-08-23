import constants as C
from node import *

#node set when we get the result while searching
RESULT_NODE = None

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

#create source node    
srcNode = Node(None, C.INPUT_STATE)
#perform iterative deepening search
iterative_deepening(srcNode)
#print the moves
getMoves()


