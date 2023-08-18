class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        temp = []
        for x,y in points:
            dist = x**2 + y**2
            temp.append([dist,[x,y]])
        temp.sort()
        for i in range(k):
            ans.append(temp[i][1])
        return ans
            
            