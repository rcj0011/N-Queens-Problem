# Homework Assignment 1 Problem 1
# All code written for COMP 6600 under Dr. Bo Liu on or before 09/20/19
# Group: Dillon Thompson, Cameron Jewell, Ethan Smyth, Naeem Ghossein

import copy
state = []

# Method for solving the N-Queens problem
# Used the hillclimbing method.
def solveNQueens(n):
    global state
    for i in range(n):
        state.append(i+1)

    # Set initial score before beginning hillclimbing
    score = scoreFunction(n, state)

    # While the score is not, zero iterate over the queens
    while score != 0:
        for q in range(n):
            # Iterate through each queens neighbors
            for nay in getNeighbors(n, state[q]):
                # Create a copy of current state
                newState = copy.deepcopy(state)
                # Alter newState with possible improvement
                newState[q] = nay
                temp = scoreFunction(n, newState)
                # If a state with a lower score is found, make that the new state.
                if temp <= score:
                    score = temp
                    state = newState
    # Print result
    print (state, score)

# Score function; it keeps track of conflicts between queens.
# Lower is better.
def scoreFunction(n, state):
    score = 0
    # Iterate through the rows and columns and calculate the score of the current state
    for q in range(n):
        for Q in range(n):
            if q != Q:
                if state[q] == state[Q] or abs(state[q]-state[Q]) == abs(q-Q):
                    score += 1

    return int(score/2)

# Returns the neighbors of the currently selected queen
# The neighbors are the squares in the provided queen's column
def getNeighbors(n, queen):
    neighbors = []
    # Go through the column of the current queen
    for i in range(1,n+1):
        # If you hit the square the queen is already in then pass over it
        if queen == i:
            pass
        # Otherwise increment the score.
        else:
            neighbors.append(i)

    return neighbors

if __name__ == "__main__":
    solveNQueens(25)
