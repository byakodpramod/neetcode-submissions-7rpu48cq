class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1,0],[0,1],[1,0],[0,-1]]
        row,col=len(grid), len(grid[0])
        result = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    continue
                count=0
                q=deque()
                q.append((i,j))
                grid[i][j]=0
                while q:
                    curX,curY=q.popleft()
                    count+=1
                    for dx,dy in directions:
                        newX,newY=curX+dx,curY+dy
                        if 0<=newX<row and 0<=newY<col and grid[newX][newY]==1:
                            q.append((newX,newY))
                            grid[newX][newY] = 0
                result = max(result, count)
        return result