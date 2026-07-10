class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for s,d in sorted(tickets)[::-1]:
            adj[s].append(d)
        # print(adj)
        stack = ["JFK"]
        res = deque()
        while stack:
            cur = stack[-1]
            if not adj[cur]:
                res.appendleft(stack.pop())
            else:
                stack.append(adj[cur].pop())
        return list(res)