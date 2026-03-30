class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row,col=len(grid),len(grid[0])
        heap, visited = [], set()
        heapq.heappush(heap, (grid[0][0],0,0))
        while heap:
            curSum,i,j=heapq.heappop(heap)
            if (i,j) in visited:
                continue
            visited.add((i,j))
            if i==row-1 and j==col-1:
                return curSum
            for a,b in [[i+1,j],[i,j+1]]:
                if 0<=a<row and 0<=b<col and (a,b) not in visited:
                    heapq.heappush(heap,(curSum+grid[a][b], a, b))
        return -1