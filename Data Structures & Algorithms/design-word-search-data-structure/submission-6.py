class WordDictionary:

    def __init__(self):
        self.root={}

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur["#"] = ""

    def search(self, word: str) -> bool:
        def dfs(cur, i):
            if i >= len(word):
                return "#" in cur
            if word[i] in cur:
                return dfs(cur[word[i]], i+1)
            elif word[i] == ".":
                for nei in cur:
                    if dfs(cur[nei], i+1):
                        return True
            return False
        return dfs(self.root, 0)
