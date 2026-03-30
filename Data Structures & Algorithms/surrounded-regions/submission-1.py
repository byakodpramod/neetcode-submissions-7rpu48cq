class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return board
        R,C=len(board), len(board[0])
        q = deque()
        for i in range(R):
            for j in range(C):
                if i == 0 or j == 0 or i == R-1 or j == C-1:
                    if board[i][j] == "O":
                        board[i][j] = "R"
                        q.append((i,j))
        # print(board)
        while q:
            x,y=q.popleft()
            for a,b in [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]:
                if 0<=a<R and 0<=b<C and board[a][b] == "O":
                    q.append((a,b))
                    board[a][b] = "R"
        for i in range(R):
            for j in range(C):
                if board[i][j] == "R":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"