queensList = []

def solveNQueens(n):
    print (n)
    initialState = []

    for i in range(n):
        initialState.append(i+1)
        q = Queen(i+1, i+1)
        queensList.append(q)

    queensList[0].setRow(3)
    getNeighbors(n, queensList[0])
    scoreFunction()

def scoreFunction():
    score = 0

    for q in queensList:
        for Q in queensList:
            if q.col != Q.col and (q.row == Q.row or abs(q.col-Q.col) == abs(q.row-Q.row)) and Q not in q.conflicts:
                score += 1
                q.conflicts.append(Q)
    
    for q in queensList:
        q.resetConflicts()

    return score

def getNeighbors(n, queen):
    neighbors = [-1,-1]
    if queen.col < n:
        neighbors[0] = queen.col + 1
    if queen.col > 0:
        neighbors[1] = queen.col - 1

    return neighbors

class Queen():
    col = 0
    row = 0
    conflicts = []

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def resetConflicts(self):
        self.conflicts = []
    
    def setRow(self, row):
        self.row = row

if __name__ == "__main__":
    solveNQueens(25)