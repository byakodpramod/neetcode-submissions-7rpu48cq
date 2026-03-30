class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        day = 0
        points = [(0,-1),(0,1),(-1,0),(1,0)]
        while q:
            x, y, day = q.popleft()
            for dx,dy in points:
                new_x, new_y = x+dx, y+dy
                if 0<=new_x<len(grid) and 0<=new_y<len(grid[0]) and grid[new_x][new_y] == 1:
                    q.append((new_x,new_y,day+1))
                    grid[new_x][new_y] = 2

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return day