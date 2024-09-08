class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        Dict = defaultdict(int)
        Dict[0] = 1
        prefixSum, count = 0, 0
        for i in range(n):
            prefixSum += nums[i]
            remove = prefixSum - k
            count += Dict[remove]
            Dict[prefixSum] += 1
    
        return count