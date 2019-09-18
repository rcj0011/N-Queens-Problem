#Assignment 1
#Group: Dillon Thompson, Cameron Jewell, Ethan Smyth, Naeem Ghossein

import copy
state = []

#this is our method for solving the 25 queens on the board
#we used the hillclimbing method.
def solveNQueens(n):
    global state
    for i in range(n):
        state.append(i+1)

    #check the score before beginning hillclimbing
    score = scoreFunction(n, state)

    #begin hillclimbing
    #while the score is not zero iterate over the queens
    while score != 0:
        #iterate through all the queens
        for q in range(n):
            #iterate through each queens neighbors
            #if a state with a lower score is found, make that the new state.
            for nay in getNeighbors(n, state[q]):
                newState = copy.deepcopy(state)
                newState[q] = nay
                temp = scoreFunction(n, newState)
                if temp <= score:
                    score = temp
                    state = newState
    #print results
    print (state, score)

#this is our score function, it keeps track of conflicts between queens.
#the lower the score, the better.
def scoreFunction(n, state):
    score = 0
    #iterate through the rows and columns and calculate the score of the current state
    for q in range(n):
        for Q in range(n):
            if q != Q:
                if state[q] == state[Q] or abs(state[q]-state[Q]) == abs(q-Q):
                    score += 1

    return int(score/2)

#this method returns the neighbors of the currently selected queen
#the neighbors are the squares in it's respective column
def getNeighbors(n, queen):
    neighbors = []
    #go through the column of the current queen
    #if you hit the square the queen is already in then pass over it
    #otherwise increment the score.
    for i in range(1,n+1):
        if queen == i:
            pass
        else:
            neighbors.append(i)

    return neighbors

if __name__ == "__main__":
    solveNQueens(25)
