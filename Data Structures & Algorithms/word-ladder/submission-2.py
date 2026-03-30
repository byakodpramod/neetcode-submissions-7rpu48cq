class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        patterns = defaultdict(list)
        visited = set()
        wordList.append(endWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                patterns[pattern].append(word)
        # print(patterns)
        q = deque([beginWord])
        visited.add(beginWord)
        res = 1
        while q:
            # print(q)
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return res
                for j in range(len(cur)):
                    pattern = cur[:j]+"*"+cur[j+1:]
                    for nei in patterns[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            res += 1
        return 0
