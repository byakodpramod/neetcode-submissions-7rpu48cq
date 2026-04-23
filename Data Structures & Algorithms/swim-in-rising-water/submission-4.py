class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        heap = [(grid[0][0], 0, 0, grid[0][0])]
        visited = set()
        res = 0
        while heap:
            curVal, i, j, pathMax = heapq.heappop(heap)
            if (i,j) in visited:
                continue
            visited.add((i,j))
            if i == len(grid)-1 and j == len(grid[0])-1:
                res = max(res, pathMax)
            for x,y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0<=x<len(grid) and 0<=y<len(grid[0]):
                    heapq.heappush(heap,(grid[x][y], x, y, max(grid[x][y], pathMax)))
        return max(res, grid[-1][-1])