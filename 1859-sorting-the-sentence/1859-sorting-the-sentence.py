class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        arr = s.split()
        for i in range(1, 10):
            for ele in arr:
                if ele[-1] == str(i):
                    ans += " "+ele[:-1]
        return ans.strip()