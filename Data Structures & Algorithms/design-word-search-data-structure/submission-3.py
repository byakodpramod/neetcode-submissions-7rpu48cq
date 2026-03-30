class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur["#"] = ""

    def search(self, word: str) -> bool:
        def helper(i,cur):
            if i >= len(word):
                return "#" in cur
            if word[i] in cur:
                return helper(i+1, cur[word[i]])
            if word[i] == ".":
                for nei in cur:
                    if helper(i+1, cur[nei]):
                        return True
            return False
        return helper(0,self.root)