class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(ocean):
            visited = set(ocean)
            q = deque(ocean)
            while q:
                i,j=q.popleft()
                for a,b in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                    if 0<=a<row and 0<=b<col and heights[a][b] >= heights[i][j] and (a,b) not in visited:
                        q.append((a,b))
                        visited.add((a,b))
            return visited

        row,col = len(heights), len(heights[0])
        pacific = [(0,y) for y in range(col)] + [(x,0) for x in range(row)]
        atlantic = [(row-1,y) for y in range(col)] + [(x, col-1) for x in range(row)]
        return sorted(bfs(pacific) & bfs(atlantic))    