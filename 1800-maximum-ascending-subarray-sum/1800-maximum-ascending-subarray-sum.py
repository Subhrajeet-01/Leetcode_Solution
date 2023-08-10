class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        add = nums[0]
        arr = []
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                add += nums[i]
            else:
                arr.append(add)
                add = nums[i]
        arr.append(add)
        return max(arr)


