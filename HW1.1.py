queensList = []

def solveNQueens(n):
    print (n)
    initialState = []

    for i in range(n):
        initialState.append(i+1)
        q = Queen(i+1, i+1)
        queensList.append(q)
    
    scoreFunction()

def scoreFunction():
    score = 0

    for q in queensList:
        for Q in queensList:
            if q.col != Q.col and (q.row == Q.row or q.col-Q.col == q.row-Q.row) and Q not in q.conflicts: #absolute value
                score += 1
                q.conflicts.append(Q)
    
    for q in queensList:
        q.resetConflicts()

    return score

def getNeighbors(queen):

    return None

class Queen():
    col = 0
    row = 0
    conflicts = []

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def resetConflicts(self):
        self.conflicts = []

if __name__ == "__main__":
    solveNQueens(25)