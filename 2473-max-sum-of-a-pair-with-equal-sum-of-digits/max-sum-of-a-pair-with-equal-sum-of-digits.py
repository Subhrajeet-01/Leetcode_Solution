class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digitSum(n):
            return sum(int(a) for a in str(n))
        
        nump = [(digitSum(num), num) for num in nums]
        nump.sort()

        maxi = -1
        for i in range(1, len(nump)):
            if nump[i][0] == nump[i - 1][0]:
                maxi = max(maxi, nump[i][1] + nump[i - 1][1])
            
        return maxi