class Solution:
    def isHappy(self, n: int) -> bool:
        def getSum(n):
            nSum = 0
            while n:
                digit = n%10
                nSum += digit * digit
                n = n // 10
            return nSum
        seen = set()
        while n not in seen:
            seen.add(n)
            n = getSum(n)
            if n == 1:
                return True
        return False
            