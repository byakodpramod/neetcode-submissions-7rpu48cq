class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return grid
        row,col,q=len(grid),len(grid[0]),deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i,j))
        dist = 1
        while q:
            for _ in range(len(q)):
                x,y = q.popleft()
                for a,b in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                    if 0<=a<row and 0<=b<col and grid[a][b] == 2147483647:
                        grid[a][b] = dist
                        q.append((a,b))
            dist += 1
        return