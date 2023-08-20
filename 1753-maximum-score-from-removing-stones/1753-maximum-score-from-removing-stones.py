class Solution(object):
    def maximumScore(self, a, b, c):

        total = a+b+c
        maxi = max(a,b,c)
        mini = min(a,b,c)
        mid = total - (maxi + mini)
        if maxi >= mini + mid:
            return mini + mid
        else: return (total)//2