class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord:
            return []
        patterns = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                patterns[pattern].append(word)
        q = deque([beginWord])
        visited = set()
        visited.add(beginWord)
        res = 1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return res
                for k in range(len(cur)):
                    cur_pattern = cur[:k]+"*"+cur[k+1:]
                    for nei in patterns[cur_pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            res += 1
        return 0