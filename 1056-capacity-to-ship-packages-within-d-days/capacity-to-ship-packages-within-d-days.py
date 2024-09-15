def findDays(weights, cap):
    days = 1  # First day
    load = 0
    n = len(weights) 
    for i in range(n):
        if load + weights[i] > cap:
            days += 1
            load = weights[i] 
        else:
            load += weights[i]
    return days

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high) // 2
            numberOfDays = findDays(weights, mid)
            if numberOfDays <= days:
                high = mid - 1
            else:                
                low = mid + 1
        return low