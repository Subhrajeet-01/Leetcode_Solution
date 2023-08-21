from collections import OrderedDict
class Solution(object):
    def sortPeople(self, names, heights):
        
        d = {}
        for i in range(len(names)):
            d[heights[i]] = names[i]
        heights.sort(reverse = True)
        for i in range(len(heights)):
            names[i] = d[heights[i]]
        return names