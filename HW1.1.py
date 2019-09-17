import copy
state = []

def solveNQueens(n):
    global state
    for i in range(n):
        state.append(i+1)

    score = scoreFunction(n, state)
    while score != 0:
        for q in range(n):
            for nay in getNeighbors(n, state[q]):
                newState = copy.deepcopy(state)
                newState[q] = nay
                temp = scoreFunction(n, newState)
                if temp <= score:
                    score = temp
                    state = newState
    
    print (state, score)

def scoreFunction(n, state):
    score = 0

    for q in range(n):
        for Q in range(n):
            if q != Q:
                if state[q] == state[Q] or abs(state[q]-state[Q]) == abs(q-Q):
                    score += 1

    return int(score/2)

def getNeighbors(n, queen):
    neighbors = []
    
    for i in range(1,n+1):
        if queen == i:
            pass
        else:
            neighbors.append(i)

    return neighbors

if __name__ == "__main__":
    solveNQueens(25)