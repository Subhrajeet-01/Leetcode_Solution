class Solution(object):
    def maximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        for n in nums:
            r |= n
        return r
        