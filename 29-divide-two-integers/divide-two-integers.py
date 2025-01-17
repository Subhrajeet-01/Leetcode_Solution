class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if dividend == -2**31 and divisor == 1:
            return -2**31
        if (dividend < 0) ^ (divisor < 0):
            sign = -1 
        else:
            sign = 1
        a = abs(dividend)
        b = abs(divisor)
        quotient = 0
        while a >= b:
            tmp = b
            m = 1
            while (tmp << 1) <= a:
                tmp <<= 1
                m <<= 1
            a -= tmp
            quotient += m
        return quotient * sign
        
        # if dividend == -2147483648 and divisor == -1:
        #     return 2147483647
        # else:
        #     division = dividend/divisor
        #     if division > 0:
        #         return floor(division)
        #     return ceil(division)