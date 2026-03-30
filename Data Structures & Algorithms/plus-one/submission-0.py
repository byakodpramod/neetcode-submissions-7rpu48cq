class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return []
        res = deque()
        carry = 1
        for i in reversed(range(len(digits))):
            curSum = digits[i]+carry
            digit = curSum % 10
            carry = curSum // 10
            res.appendleft(digit)
        if carry != 0:
            res.appendleft(carry)
        return list(res)