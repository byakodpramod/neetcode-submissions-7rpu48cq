class Solution:
    def tribonacci(self, n: int) -> int:
        def helper(n,store):
            if n in store:
                return store[n]
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
            store[n] = helper(n-1, store) + helper(n-2, store) + helper(n-3, store)
            return store[n]
        return helper(n,{})