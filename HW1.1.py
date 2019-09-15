def solveNQueens(n):
    print (n)
    numQueens = 0
    initialState = []
    queensList = []

    for i in range(n):
        initialState.append(i+1)
        q = Queen(i, i+1)
        queensList.append(q)

def scoreFunction():
    score = 0



    return score

def getNeighbors(queen):

    return None

class Queen():
    column = 0
    row = 0

    def __init__(self, row, col):
        self.row = row
        self.column = col

if __name__ == "__main__":
    solveNQueens(25)