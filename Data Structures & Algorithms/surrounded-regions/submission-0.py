class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1:
                    if board[i][j] == "O":
                        board[i][j] = "R"
                        q.append([i,j])
        while q:
            x,y = q.popleft()
            for direction in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_x,new_y=x+direction[0],y+direction[1]
                if 0<=new_x<len(board) and 0<=new_y<len(board[0]) and board[new_x][new_y]=='O':
                    board[new_x][new_y] = "R"
                    q.append([new_x,new_y])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"        