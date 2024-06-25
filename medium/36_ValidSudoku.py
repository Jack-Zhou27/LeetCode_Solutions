class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashSet = set()
        for i in range(9):
            for j in range(9):
                if(board[i][j] != "."):
                    if((i, board[i][j]) in hashSet or (board[i][j], j) in hashSet or (100 + i // 3 + (j // 3) * 3, board[i][j]) in hashSet):
                        return False
                    hashSet.add((i, board[i][j]))
                    hashSet.add((board[i][j], j))
                    hashSet.add((100 + i // 3 + (j // 3) * 3, board[i][j])) #note that 100 + i // 3 + (j // 3) * 3 ensures we have a unique identification for what grid we are in
                    
        return True
