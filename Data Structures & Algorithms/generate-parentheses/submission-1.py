class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(leftCount, rightCount, slate):
            if leftCount == n and rightCount == n:
                res.append("".join(slate))
                return
            if leftCount < n:
                slate.append("(")
                helper(leftCount+1, rightCount, slate)
                slate.pop()
            if rightCount < leftCount:
                slate.append(")")
                helper(leftCount, rightCount+1, slate)
                slate.pop()
        res = []
        helper(0,0,[])
        return res