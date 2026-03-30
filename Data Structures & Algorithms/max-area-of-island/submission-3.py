class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    q = deque()
                    q.append((x,y))
                    area = 0
                    grid[x][y] = 0
                    while q:
                        i,j=q.popleft()
                        area += 1
                        for a,b in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
                            if 0<=a<len(grid) and 0<=b<len(grid[0]) and grid[a][b] == 1:
                                q.append((a,b))
                                grid[a][b] = 0
                    res = max(res, area)
        return res
                    