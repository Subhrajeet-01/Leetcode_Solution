class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones)>1:
            
            y = max(stones)
            stones.remove(y)
            x = max(stones)
            stones.remove(x)
            if x != y:
                z = abs(x-y)
                stones.append(z)
        if stones:
            return stones[0]
        return 0
        