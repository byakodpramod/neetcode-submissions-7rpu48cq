class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0
        heap, R, C = [], len(heights), len(heights[0])
        heapq.heappush(heap,(0,0,0))
        visited = set()
        while heap:
            curDiff,i,j = heapq.heappop(heap)
            if (i,j) in visited:
                continue
            visited.add((i,j))
            if i == R-1 and j == C-1:
                # print(i,j, curDiff)
                return curDiff
            for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=x<R and 0<=y<C and (x,y) not in visited:
                    newDiff = max(curDiff, abs(heights[i][j] - heights[x][y]))
                    heapq.heappush(heap, (newDiff, x,y))
        return 0