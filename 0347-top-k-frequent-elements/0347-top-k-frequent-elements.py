class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        s=set(nums)
        l=list(s)
        L=[]
        result=[]
        for i in range(len(l)):
            n=nums.count(l[i])
            L.append(n)
        for i in range(k):
            maxi=max(L)
            ind=L.index(maxi)
            result.append(l[ind])
            L[ind]=0
        return result
