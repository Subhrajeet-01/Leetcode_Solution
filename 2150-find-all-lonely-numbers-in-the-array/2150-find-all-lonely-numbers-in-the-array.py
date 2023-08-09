class Solution(object):
    def findLonely(self, nums):
        ans, dic = [], {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else: 
                dic[n] += 1
        for n in dic:
            if dic[n] == 1 and n-1 not in dic and n+1 not in dic:
                ans.append(n)
        return ans
