class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        itemcount = dict()
        total = 0
        for i in nums:
            if i in itemcount:
                itemcount[i] += 1
            else:
                itemcount[i] = 1
        for i,j in itemcount.items():
            if j > 1:
                total += j * (j-1) // 2
        return total