class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def backtrack(start, cur, target):
            if target == 0:
                res.append(cur[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break

                cur.append(candidates[i])
                backtrack(i+1, cur, target - candidates[i])
                cur.pop()

        backtrack(0, [], target)
        return res