class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(i, slate):
            if len(slate) == k:
                res.append(slate[:])
                return
            if i > n:
                return
            dfs(i+1, slate)
            slate.append(i)
            dfs(i+1, slate)
            slate.pop()
        res = []
        dfs(1,[])
        return res