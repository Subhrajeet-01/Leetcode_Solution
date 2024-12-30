class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        memo = {}
        def dfs(i, prev):
            if i == len(nums):
                return []
            
            if (i, prev) in memo:
                return memo[(i, prev)]
            
            res = dfs(i + 1, prev)
            if prev == 1 or nums[i] % prev == 0:
                tmp = [nums[i]] + dfs(i + 1, nums[i])
                if len(tmp) > len(res):
                    res = tmp
            
            memo[(i, prev)] = res
            return res

        return dfs(0, 1)