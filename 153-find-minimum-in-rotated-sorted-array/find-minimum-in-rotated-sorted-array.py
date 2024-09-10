class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        ans = nums[high]
        while low <= high:
            mid = (low + high) // 2
            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                low = mid + 1
            else:
                high = mid - 1
                ans = min(ans, nums[mid])
        return ans