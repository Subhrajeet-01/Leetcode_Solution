class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        arr = Counter(nums)
        for val in arr.values():
            if val % 2 == 1:
                return False

        return True