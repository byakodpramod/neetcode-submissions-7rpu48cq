class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q = deque()
                    q.append([i,j,0])
                    visited = set((i,j))
                    directions = [[0,1],[0,-1],[1,0],[-1,0]]
                    while q:
                        r,c,dist=q.popleft()
                        if grid[r][c] != -1 or grid[r][c] != 0:
                            grid[r][c] = min(grid[r][c],dist)
                        for x,y in directions:
                            new_R,new_C=r+x,c+y
                            if 0<=new_R<len(grid) and 0<=new_C<len(grid[0]) and (new_R,new_C) not in visited and (grid[new_R][new_C] != -1 and grid[new_R][new_C] != 0):
                                visited.add((new_R,new_C))
                                q.append([new_R,new_C,dist+1])
        return grid