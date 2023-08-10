class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        overal_max,current_max = nums[0],nums[0]
        for i in range(1,len(nums)):
            current_max = max(nums[i], nums[i]+current_max)
            overal_max = max(overal_max, current_max)
        return overal_max


        