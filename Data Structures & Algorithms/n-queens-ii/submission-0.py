class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(r):
            if r >= n:
                res[0] += 1
                return
            for c in range(n):
                if c in cols or r+c in posDiag or r-c in negDiag:
                    continue
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                grid[r][c] = "Q"
                dfs(r+1)
                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                grid[r][c] = "."
        if not n:
            return 0
        grid, res = [["."] * n for _ in range(n)], [0]
        cols, posDiag, negDiag = set(), set(), set()
        dfs(0)
        return res[0]