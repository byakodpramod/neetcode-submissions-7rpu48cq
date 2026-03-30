class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,idx,visited):
            if idx == len(word):
                return True
            if idx >= len(word) or i<0 or i>=R or j<0 or j>=C or board[i][j] != word[idx] or (i,j) in visited:
                return False
            visited.add((i,j))
            res = False
            res = dfs(i+1,j,idx+1,visited) or dfs(i-1,j,idx+1,visited) or dfs(i,j+1,idx+1,visited) or dfs(i,j-1,idx+1,visited)
            visited.remove((i,j))
            return res
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