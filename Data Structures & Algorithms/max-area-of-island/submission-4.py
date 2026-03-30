class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
        if not grid:
            return 0
        res = 0
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if grid[a][b] == 1:
                    res = max(res, dfs(a,b))
        return res