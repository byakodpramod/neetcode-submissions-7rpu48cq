class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        # if not piles:
        #     return True
        # cache = {}
        # def dfs(i,j,p1,p2,aTurn):
        #     if i > j:
        #         return p1 >= p2
        #     if (i,j,p1,p2,aTurn) in cache:
        #         return cache[(i,j,p1,p2,aTurn)]
        #     ans = False
        #     if aTurn:
        #         ans = dfs(i+1,j,p1+piles[i],p2,False) or dfs(i,j-1,p1+piles[j],p2,False)
        #     else:
        #         ans = dfs(i+1,j,p1,p2+piles[i],True) and dfs(i,j-1,p1,p2+piles[j],True)
        #     cache[(i,j,p1,p2,aTurn)] = ans
        #     return ans
        # return dfs(0,len(piles)-1,0,0,True)