class Solution:
    def bfs(self,heights,ocean,R,C):
        q = deque(ocean)
        visited = set(ocean)
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            r,c=q.popleft()
            for x,y in directions:
                newX,newY=r+x,c+y
                if 0<=newX<R and 0<=newY<C and (newX,newY) not in visited and heights[newX][newY] >= heights[r][c]:
                    q.append((newX,newY))
                    visited.add((newX,newY))
        return visited

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        R = len(heights)
        C = len(heights[0])
        pacificVisited = [(0,i) for i in range(C)] + [(j,0) for j in range(1,R)]
        atlanticVisited = [(i,C-1) for i in range(R)] + [(R-1,j) for j in range(C-1)]
        # print(pacificVisited)
        # print(atlanticVisited)
        return sorted(self.bfs(heights,pacificVisited,R,C) & self.bfs(heights,atlanticVisited,R,C))