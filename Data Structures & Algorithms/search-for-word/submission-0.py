class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x,y,visited,idx):
            if idx == len(word):
                return True
            found = False
            if 0<=x<len(board) and 0<=y<len(board[0]) and (x,y) not in visited and board[x][y] == word[idx]:
                visited.add((x,y))
                found = dfs(x+1, y, visited, idx+1) or dfs(x-1, y, visited, idx+1) or dfs(x, y+1, visited, idx+1) or dfs(x, y-1, visited, idx+1)
                visited.remove((x,y))
            return found
        visited=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i,j,visited,0):
                        return True
        return False