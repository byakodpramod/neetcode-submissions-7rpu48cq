"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        q = deque()
        q.append(head)
        store = {}
        while q:
            curNode = q.popleft()
            if curNode not in store:
                store[curNode] = Node(curNode.val)
            if curNode.random and curNode.random not in store:
                store[curNode.random] = Node(curNode.random.val)
                q.append(curNode.random)
            if curNode.next and curNode.next not in store:
                store[curNode.next] = Node(curNode.next.val)
                q.append(curNode.next)
            store[curNode].next = store.get(curNode.next)
            store[curNode].random = store.get(curNode.random)
        return store[head]