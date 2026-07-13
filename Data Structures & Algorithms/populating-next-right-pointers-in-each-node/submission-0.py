"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q = deque([root])
        while q:
            prev = None
            for i in range(len(q)):
                cur = q.popleft()
                if i != 0 and prev:
                    prev.next = cur
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                prev = cur
        return root