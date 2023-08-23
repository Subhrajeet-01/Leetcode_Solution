class Solution(object):
    def findScore(self, nums):
        
        n = len(nums)
        score = 0
        marked = [False] * n
        q = [(nums[i], i) for i in range(n)]
        heapq.heapify(q)
        while q:
            val, idx = heapq.heappop(q)
            if not marked[idx]:
                score += val
                marked[idx] = True
                if idx > 0:
                    marked[idx-1] = True
                if idx < n-1:
                    marked[idx+1] = True
        return score
        
        