class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(r):
            if r == n:
                res.append(["".join(k) for k in board])
                return
            for c in range(n):
                if c in col or (r-c) in negDiag or (r+c) in posDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = 'Q'
                dfs(r+1)
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]
        dfs(0)
        return res