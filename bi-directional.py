from typing_extensions import get_args
import constants as C
from node import *


def bi_directional_search(srcNode, goalNode):

    queue_src_to_goal = []
    queue_goal_to_src = []
    visited = set()
    visited.add(srcNode)

    queue_src_to_goal.append(srcNode)
    queue_goal_to_src.append(goalNode)

    while len(queue_goal_to_src)!=0 and len(queue_src_to_goal)!=0:

        node = queue_goal_to_src.pop(0)
        
        for ele in visited:
            
            if ele.state == node.state:
                return node, ele
       
        else:
            succ = node.getSuccesors()
        
            for s in succ:
                
                queue_goal_to_src.append(s)
            node = queue_src_to_goal.pop(0)
            succ = node.getSuccesors()
            
            for s in succ:
                if s not in visited:
                    queue_src_to_goal.append(s)
                    visited.add(s)
            

    return False

def getMoves(node1, node2):

    FORWARD_MOVES = []
    BACKWARD_MOVES = []
    curr = node1

    while curr is not None:
        FORWARD_MOVES.append(curr)
        curr = curr.parent

    curr = node2.parent

    while curr is not None:
        BACKWARD_MOVES.append(curr)
        curr = curr.parent

    SOLUTION_MOVES = []

    while len(BACKWARD_MOVES)!=0:
        SOLUTION_MOVES.append(BACKWARD_MOVES.pop())

    while len(FORWARD_MOVES)!=0:
        SOLUTION_MOVES.append(FORWARD_MOVES.pop(0))

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

