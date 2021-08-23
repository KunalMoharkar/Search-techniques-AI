import constants as C
from node import *

#list cannot be hashed 
#todo store states into visited as tuples to enable hashing 
#function to check if current node has already been visited
def check_visited(node, visited):

    for ele in visited: 
        if ele.state == node.state:
            return ele

    return False

#Bidirectional search
def bi_directional_search(srcNode, goalNode):

    queue_src_to_goal = []
    queue_goal_to_src = []
    visited = set()
    visited.add(srcNode)

    queue_src_to_goal.append(srcNode)
    queue_goal_to_src.append(goalNode)

    while len(queue_goal_to_src)!=0 and len(queue_src_to_goal)!=0:

        #check if node in backward search is already visited in forward search
        node = queue_goal_to_src.pop(0)
        res = check_visited(node,visited)
        if res:
            return node, res

        else:
            #backward search
            succ = node.getSuccesors()
        
            for s in succ:  
                queue_goal_to_src.append(s)

            #forward search
            node = queue_src_to_goal.pop(0)
            succ = node.getSuccesors()
            
            for s in succ:
                #keep track of visited nodes in forward search
                if s not in visited:
                    queue_src_to_goal.append(s)
                    visited.add(s)
            
    return False

#print the sequence of moves
def getMoves(node1, node2):

    FORWARD_MOVES = []
    BACKWARD_MOVES = []

    #store the moves from intersection node to goal node
    curr = node1
    while curr is not None:
        FORWARD_MOVES.append(curr)
        curr = curr.parent

    #backtrack the moves from interseaction node to src node
    curr = node2.parent
    while curr is not None:
        BACKWARD_MOVES.append(curr)
        curr = curr.parent

    #merge the moves
    SOLUTION_MOVES = []

    while len(BACKWARD_MOVES)!=0:
        SOLUTION_MOVES.append(BACKWARD_MOVES.pop())

    while len(FORWARD_MOVES)!=0:
        SOLUTION_MOVES.append(FORWARD_MOVES.pop(0))

    #print the exact moves
    start_node = SOLUTION_MOVES.pop(0)
    prev_pos = start_node.getBlankTile()
    start_node.printNode()

    for x in SOLUTION_MOVES:
        curr_pos = x.getBlankTile()
    
        print(f"\n\nmove blank from {prev_pos} to {curr_pos}")
    
        prev_pos = curr_pos
        x.printNode()


#create source node    
srcNode = Node(None, C.INPUT_STATE)
#create goal node
goalNode = Node(None, C.GOAL_STATE)


res = bi_directional_search(srcNode,goalNode)


print("\n-----------------------------------------------INITIAL STATE--------------------------------------")
srcNode.printNode()

print("\n-----------------------------------------------GOAL STATE--------------------------------------")
goalNode.printNode()

if res:
    print("\n-------------------------------------------INTERSECTION STATE--------------------------------------")
    res[0].printNode()

    print("\n-------------------------------------------MOVES SEQUENCE--------------------------------------")
    getMoves(res[0],res[1])

else:

    print("GIVEN PUZZLE IS NOT SOLVABLE")

