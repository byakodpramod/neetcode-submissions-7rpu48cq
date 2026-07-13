# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(cur, curSum):
            if not cur:
                return False
            curSum += cur.val
            if cur.left is None and cur.right is None and curSum == targetSum:
                return True
            return dfs(cur.left, curSum) or dfs(cur.right, curSum)
        return dfs(root, 0)