class Solution(object):
    def topKFrequent(self, words, k):

        words = list(sorted(words))
        h = {}
        for i in words:
            if i not in h:
                h[i] = 1
            else:
                h[i] += 1
        
        a = sorted(h, key = lambda x: (-h[x],x))
        print(type(a))
        return a[:k]
        


        