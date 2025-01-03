class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        count = 0
        left = nums[0]
        for i in range(1, len(nums)):
            right = total - left
            if left >= right:
                count += 1
            left = left + nums[i]
        
        return count

