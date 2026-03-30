class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, idx, visited):
            if idx == len(word):
                return True
            isFound = False
            if 0<=i<row and 0<=j<col and board[i][j] == word[idx] and (i,j) not in visited:
                visited.add((i,j))
                isFound = dfs(i+1, j, idx+1, visited) or dfs(i-1, j, idx+1, visited) or dfs(i, j+1, idx+1, visited) or dfs(i, j-1, idx+1, visited)
                visited.remove((i,j))
            return isFound

        row, col = len(board), len(board[0])
        visited = set()
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, visited):
                        return True
        return False