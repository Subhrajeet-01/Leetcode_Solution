
def calculateTotalHours(piles, hourly):
    totalH = 0
    n = len(piles)
    # Find total hours
    for i in range(n):
        totalH += math.ceil(piles[i] / hourly)
    return totalH
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi = max(piles)
        low = 1
        high = maxi

        # Apply binary search
        while low <= high:
            mid = (low + high) // 2
            totalH = calculateTotalHours(piles, mid)
            if totalH <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low

        