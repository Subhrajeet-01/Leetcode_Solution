class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            lar = sma = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] < sma:
                    sma = nums[j]
                if nums[j] > lar:
                    lar = nums[j]

                res += (lar - sma)
            
        return res