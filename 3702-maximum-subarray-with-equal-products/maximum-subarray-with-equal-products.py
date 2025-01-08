from math import gcd, lcm
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        N = len(nums)
        ret = 0
        for i in range(N):
            g, l, p = 0, 1, 1
            for j in range(i, N):
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])
                p *= nums[j]
                if p == l * g:
                    ret = max(ret, j - i + 1)
        return ret
