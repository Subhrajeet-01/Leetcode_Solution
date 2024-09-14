def possible(arr, day, m, k):
    n = len(arr)  
    cnt = 0
    noOfB = 0
    # count the number of bouquets
    for i in range(n):
        if arr[i] <= day:
            cnt += 1
        else:
            noOfB += cnt // k
            cnt = 0
    noOfB += cnt // k
    return noOfB >= m

class Solution:
    def minDays(self, arr: List[int], m: int, k: int) -> int:
        val = m * k
        n = len(arr)  
        if val > n:
            return -1
        low = min(arr)
        high = max(arr)
        while low <= high:
            mid = (low + high) // 2
            if possible(arr, mid, m, k):
                high = mid - 1
            else:
                low = mid + 1
        return low