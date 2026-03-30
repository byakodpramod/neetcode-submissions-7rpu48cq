class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return []
        row,col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q = deque()
                    visited = set((i,j))
                    q.append((i,j,0))
                    while q:
                        x,y,dist = q.popleft()
                        if grid[x][y] != 0 or grid[x][y] != -1:
                            grid[x][y] = min(grid[x][y], dist)
                        for a,b in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                            if 0<=a<row and 0<=b<col and grid[a][b] != -1 and grid[a][b] != 0 and (a,b) not in visited:
                                q.append((a,b,dist+1))
                                visited.add((a,b))