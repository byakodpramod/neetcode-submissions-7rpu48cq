class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        heap = []
        heap.append((grid[0][0], 0, 0, grid[0][0]))
        heapq.heapify(heap)
        visited = set()
        visited.add((0,0))
        while heap:
            curVal, r, c, maxUntil= heapq.heappop(heap)
            # print(curVal, r, c, maxUntil)
            if r == len(grid)-1 and c == len(grid[0])-1:
                return max(maxUntil, curVal)
            for x,y in [[0,1], [1,0], [0,-1], [-1,0]]:
                new_x, new_y = x+r, y+c
                if 0<=new_x<len(grid) and 0<=new_y<len(grid[0]) and (new_x,new_y) not in visited:
                    visited.add((new_x,new_y))
                    heapq.heappush(heap, (grid[new_x][new_y], new_x, new_y, max(maxUntil, grid[new_x][new_y])))
        return -1