class Solution(object):
    def minNumber(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1.sort()
        nums2.sort()
        for i in nums1:
            if i in nums2:
                return int(i)
        
        
        x=str(min(nums1))
        y=str(min(nums2))
        z=x+y
        q=y+x
        x=min(int(z),int(q))
        return x
        