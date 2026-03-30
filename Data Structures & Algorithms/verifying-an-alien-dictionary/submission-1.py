class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDic = {c:i for i,c in enumerate(order)}
        # print(orderDic)
        def verify(s1,s2):
            i,j=0,0
            while i<len(s1) and j<len(s2):
                if orderDic[s1[i]] == orderDic[s2[j]]:
                    i+=1
                    j+=1
                elif orderDic[s1[i]] < orderDic[s2[j]]:
                    return True
                else:
                    return False
            if len(s1) > len(s2):
                return False
            return True
        
        for x in range(len(words)-1):
            w1 = words[x]
            w2 = words[x+1]
            if not verify(w1, w2):
                return False
        return True