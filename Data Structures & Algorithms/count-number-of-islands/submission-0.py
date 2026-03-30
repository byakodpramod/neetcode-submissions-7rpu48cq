class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row,col=len(grid), len(grid[0])
        islandCount=0
        directions=[[0,-1],[0,1],[-1,0],[1,0]]
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    islandCount+=1
                    q=deque()
                    q.append((r,c))
                    grid[r][c]="0"
                    while q:
                        curX,curY=q.popleft()
                        for dx,dy in directions:
                            newX,newY=curX+dx,curY+dy
                            if 0<=newX<row and 0<=newY<col and grid[newX][newY]=="1":
                                q.append((newX,newY))
                                grid[newX][newY] = "0"
        return islandCount