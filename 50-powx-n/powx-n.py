class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        num = n
        if num < 0:
            num = -1 * num
        while num:
            if num % 2 == 1:
                ans = ans * x
                num -= 1
            else:
                x *= x
                num //= 2
        if n < 0:
            ans = 1.0 / ans
        return ans