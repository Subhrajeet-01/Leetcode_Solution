class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            c = 0
            for j in range(nums2.index(i), len(nums2)):
                if(nums2[j]>i):
                    ans.append(nums2[j])
                    c += 1
                    break
            if c==0:
                ans.append(-1)
                
        return ans
