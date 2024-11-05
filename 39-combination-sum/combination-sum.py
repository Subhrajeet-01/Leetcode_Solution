class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, cur, target):
            if target == 0:
                res.append(cur[:])
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                
                cur.append(candidates[i])
                backtrack(i, cur, target - candidates[i])
                cur.pop()
        
        backtrack(0, [], target)
        return res
                
            