class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x:
            pop = x % 10
            x //= 10
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
                return 0
            rev = rev * 10 + pop
        rev *= sign
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev
