class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []
        result, stack, adj = deque(), ["JFK"], defaultdict(list)
        for s,d in reversed(sorted(tickets)):
            adj[s].append(d)
        while stack:
            cur = stack[-1]
            if not adj[cur]:
                result.appendleft(stack.pop())
            else:
                stack.append(adj[cur].pop())
        return list(result)