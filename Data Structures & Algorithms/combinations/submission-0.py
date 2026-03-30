class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(i,slate):
            if len(slate) == k:
                res.append(slate[:])
                return
            for j in range(i,n+1):
                slate.append(j)
                helper(j+1, slate)
                slate.pop()
        res = []
        helper(1,[])
        return res