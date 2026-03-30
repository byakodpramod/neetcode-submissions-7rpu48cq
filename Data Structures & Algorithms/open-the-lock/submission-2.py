class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def getChildren(key):
            children = []
            for i in range(len(key)):
                nextNum = (int(key[i]) + 1) % 10
                prevNum = (int(key[i]) - 1 + 10) % 10
                children.append(key[:i]+str(nextNum)+key[i+1:])
                children.append(key[:i]+str(prevNum)+key[i+1:])
            return children
        if "0000" in deadends:
            return -1
        visited = set(deadends)
        visited.add("0000")
        res = float("inf")
        q = deque()
        q.append(("0000", 0))
        while q:
            cur, steps = q.popleft()
            if cur == target:
                res = min(res, steps)
            for nei in getChildren(cur):
                if nei not in visited:
                    q.append((nei, steps+1))
                    visited.add(nei)
        return res if res != float('inf') else -1