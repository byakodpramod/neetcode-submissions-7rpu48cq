class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                graph[pattern].append(word)
        q = deque([beginWord])
        visited=set()
        res = 1
        while q:
            for _ in range(len(q)):
                curWord = q.popleft()
                if curWord == endWord:
                    return res
                for i in range(len(curWord)):
                    pattern = curWord[:i]+"*"+curWord[i+1:]
                    for nei in graph[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            res += 1
        return 0