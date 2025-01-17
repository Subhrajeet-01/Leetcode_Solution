class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result = start ^ goal
        ans = 0
        while result > 0:
            ans += result & 1
            result >>= 1
        
        return ans