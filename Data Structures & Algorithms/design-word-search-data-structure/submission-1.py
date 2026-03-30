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
        def dfs(node, i):
            if i >= len(word):
                return "#" in node
            if word[i] == '.':
                for child in node:
                    if dfs(node[child], i + 1):
                        return True 
            if word[i] in node:
                return dfs(node[word[i]], i + 1)
            return False
        return dfs(self.root, 0)
        
