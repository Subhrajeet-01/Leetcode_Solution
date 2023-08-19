class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        val = []
        for i in arr:
            val.append([abs(x-i),i])
        ans = []
        for i in sorted(val,key = lambda x:x[0]):
            k -= 1
            ans.append(i[1])
            if k == 0: break
        return sorted(ans)


            
