class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        num1 = 1
        num2 = 1
        if n == 1 or n == 2:
            return n
        for i in range(n - 1):
            num3 = num1 + num2
            num1 = num2
            num2 = num3
        return num2