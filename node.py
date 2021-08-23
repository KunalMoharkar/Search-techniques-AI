import copy
import constants as C


#node class with members as current state and parent pointer
class Node:
    def __init__(self, parent, state):
        self.parent = parent
        self.state = state

    def isGoalNode(self):
        return C.GOAL_STATE == self.state

    def printNode(self):
        n = len(self.state)

        for i in range(n):
            print()
            for j in range(n):

                print(self.state[i][j], end="  ")

    #generate succesors of a node
    #also sets the parent pointers accordingly
    def getSuccesors(self):

        res = []
        for move in C.MOVES:
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
        #deepcopy to avoid reference value modification
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

        #return the new state
        return copy_mat


