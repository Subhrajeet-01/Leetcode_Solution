class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i = max(nums)
        return nums.index(i)
        
        