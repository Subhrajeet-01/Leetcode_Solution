class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        count = 0
        for ele in operations:
            if ele == "++X" or ele == "X++":
                count += 1
            else:
                count -= 1
        return count

        