class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        time = 0
        q = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i,j,0))
        while q:
            x,y,time = q.popleft()
            for a,b in [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]:
                if 0<=a<row and 0<=b<col and grid[a][b] == 1:
                    q.append((a,b,time+1))
                    grid[a][b] = 2
        for m in range(row):
            for n in range(col):
                if grid[m][n] == 1:
                    return -1
        return time
