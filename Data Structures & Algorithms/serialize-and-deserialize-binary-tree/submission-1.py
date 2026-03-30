# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        return str(root.val)+","+self.serialize(root.left)+self.serialize(root.right) if root else "#,"
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        q = deque(data.split(","))
        q.pop()
        def helper(root):
            item = q.popleft()
            if item == "#":
                return None
            root = TreeNode(item)
            root.left = helper(root)
            root.right = helper(root)
            return root
        return helper(None)