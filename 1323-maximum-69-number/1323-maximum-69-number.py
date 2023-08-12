class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        j = ''
        t = True
        for i in s:
            if i == '6' and t:
                j += '9'
                t = False
            else:
                j += i
            
        return int(j)