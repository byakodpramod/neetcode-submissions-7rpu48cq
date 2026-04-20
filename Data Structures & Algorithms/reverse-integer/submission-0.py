class Solution:
    def reverse(self, x: int) -> int:
        x_str = list(str(x)) if x > 0 else list(str(-1*x))
        i,j = 0,len(x_str)-1
        while i<j:
            x_str[i],x_str[j] = x_str[j],x_str[i]
            i += 1
            j -= 1
        x = int("".join(x_str)) if x>0 else -1*int("".join(x_str))
        if x < -(1 << 31) or x > (1 << 31) - 1:
            return 0
        return x