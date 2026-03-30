# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return 0
            leftSum = max(helper(root.left),0)
            rightSum = max(helper(root.right),0)
            res[0] = max(res[0], leftSum+rightSum+root.val)
            return max(leftSum, rightSum) + root.val
        res = [float("-inf")]
        helper(root)
        return res[0]