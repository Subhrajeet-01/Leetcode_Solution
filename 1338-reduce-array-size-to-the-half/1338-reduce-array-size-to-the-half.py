from collections import OrderedDict
class Solution(object):
    def minSetSize(self, arr):

        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        f = sorted(d.values(),reverse = True)
        l = len(arr) // 2
        ans = 0
        while l > 0:
            l -= f[ans]
            ans += 1
        return ans
        
        print(d)
        
        
                