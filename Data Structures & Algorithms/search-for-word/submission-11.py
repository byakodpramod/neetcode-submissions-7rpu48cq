class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,idx,visited):
            if idx >= len(word):
                return True
            if not 0<=i<len(board) or not 0<=j<len(board[0]) or word[idx] != board[i][j] or (i,j) in visited:
                return False
            isFound = False
            visited.add((i,j))
            isFound = dfs(i+1,j,idx+1,visited) or dfs(i-1,j,idx+1,visited) or dfs(i,j+1,idx+1,visited) or dfs(i,j-1,idx+1,visited)
            visited.remove((i,j))
            return isFound
        
        if not word:
            return True
        R, C = len(board), len(board[0])
        visited, idx = set(), 0
        for i in range(R):
            for j in range(C):
                if board[i][j] == word[idx]:
                    if dfs(i,j,idx,visited):
                        return True
        return False