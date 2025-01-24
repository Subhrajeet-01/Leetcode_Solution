class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums) // 3
        hashmap = Counter(nums)
        for key, value in hashmap.items():
            if value > n:
                ans.append(key)
        return ans