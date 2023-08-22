import math
class Solution(object):
    def maximumProduct(self, A, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapify(A)
        for i in range(k):
            heappush(A, heappop(A) + 1)
        res=1
        for x in A:
            res=(res*x)%(10**9+7)
        return res
        
            
        

