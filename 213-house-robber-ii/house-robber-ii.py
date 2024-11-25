class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def linearRob(i, j):
            prev1, prev2 = 0, 0
            for num in range(i, j):
                current = max(prev1, prev2 + nums[num])
                prev2, prev1 = prev1, current
            return max(prev1, prev2)
        
        if n == 1: 
            return nums[0]
        else: 
            return max(linearRob(0,n-1), linearRob(1,n))