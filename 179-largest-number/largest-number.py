class Solution : 
    def largestNumber(self, nums: List[int]) -> str :
        nums = list(map(str, nums))
        i = 0
        j = i + 1
        while i <= len(nums) :
            while j < len(nums) :
                if int(nums[i] + nums[j]) < int(nums[j] + nums[i]) :
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
                
            i += 1
            j = i + 1
        return str(int(''.join(nums)))