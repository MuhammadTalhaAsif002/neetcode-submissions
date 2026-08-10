class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[]
        col=[]
        box={(0,0):set(),(0,1):set(),(0,2):set(),(1,0):set(),  
        (1,1):set(),(1,2):set(),(2,0):set(),(2,1):set(),
        (2,2):set()}
        for i in range(0,9,1):
            row.append(set())
            col.append(set())

        for i in range(9):
            for j in range(9):
                key = (i // 3, j // 3)
                if board[i][j] == ".":
                    continue
                print(i, j, board[i][j], key, box[key])

                if board[i][j] in box[key]:
                    return False
                box[key].add(board[i][j])

                if board[i][j] in row[i]:
                    return False

                if board[i][j] in col[j]:
                    return False

                row[i].add(board[i][j])
                col[j].add(board[i][j])
    
        return True