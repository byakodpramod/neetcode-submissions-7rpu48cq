class Trie:
    def __init__(self):
        self.root = {}
    
    def addWord(self, word):
        cur = self.root
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur["#"] = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C, result = len(board), len(board[0]), set()
        trie = Trie()
        for word in words:
            trie.addWord(word)

        def dfs(r,c,node,visited,word):
            if not 0<=r<R or not 0<=c<C or (r,c) in visited or board[r][c] not in node:
                return
            visited.add((r,c))
            node = node[board[r][c]]
            word += board[r][c]
            if "#" in node:
                result.add(word)
            dfs(r+1,c,node,visited,word)
            dfs(r-1,c,node,visited,word)
            dfs(r,c+1,node,visited,word)
            dfs(r,c-1,node,visited,word)
            visited.remove((r,c))
            # word.pop()
    

        for i in range(R):
            for j in range(C):
                dfs(i,j,trie.root,set(),"")
        return list(result)
