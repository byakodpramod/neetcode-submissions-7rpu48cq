class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def bfs(r,c):
            res = 0
            q.append((r,c))
            visited = set()
            visited.add((r,c))
            while q:
                a,b = q.popleft()
                for x,y in [[a+1,b], [a-1,b], [a,b+1], [a,b-1]]:
                    if (x<0 or y<0 or x>=ROW or y>=COL or grid[x][y] == 0):
                        res += 1
                    elif (x,y) not in visited:
                        visited.add((x,y))
                        q.append((x,y))
            return res
        if not grid:
            return 0
        q, ROW, COL = deque(),len(grid), len(grid[0])
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    return bfs(i,j)
        return 0