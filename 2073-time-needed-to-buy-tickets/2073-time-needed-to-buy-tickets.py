class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(tickets)):
            if tickets[i] >= tickets[k]:
                if k < i:
                    count += tickets[k]-1
                else:
                    count += tickets[k]
            else:
                count += tickets[i]
            
        return count