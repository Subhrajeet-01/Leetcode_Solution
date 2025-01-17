class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for i in range(1 << n):
            subset = []
            for j in range(n):
                if i & (1 << j):
                    subset.append(nums[j])
            res.append(subset)

        return res

        # res = []
        # subset = []

        # def dfs(i):
        #     if i >= len(nums):
        #         res.append(subset.copy())
        #         print(res)
        #         return
            
        #     subset.append(nums[i])
        #     dfs(i + 1)

        #     subset.pop()
        #     dfs(i + 1)
        # dfs(0)
        
        return res