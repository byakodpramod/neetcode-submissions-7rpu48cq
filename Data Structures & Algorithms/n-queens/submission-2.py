class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(r):
            if r == n:
                res.append(["".join(k) for k in board])
                return
            for c in range(n):
                if c in col or r+c in posDig or r-c in negDig:
                    continue
                board[r][c] = "Q"
                col.add(c)
                posDig.add(r+c)
                negDig.add(r-c)
                dfs(r+1)
                board[r][c] = "."
                col.remove(c)
                posDig.remove(r+c)
                negDig.remove(r-c)

        if not n:
            return []
        res, col, posDig, negDig = [], set(), set(), set()
        board = [["."] * n for _ in range(n)]
        dfs(0)
        return res