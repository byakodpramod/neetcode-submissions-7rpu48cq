class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return True
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                element = board[i][j]
                if element == ".":
                    continue
                if element in row[i] or element in col[j] or element in square[(i//3, j//3)]:
                    return False
                row[i].add(element)
                col[j].add(element)
                square[(i//3,j//3)].add(element)
        return True