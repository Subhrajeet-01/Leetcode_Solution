class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr = [i for i in range(1, 10)]
        res = []

        def backtrack(start, cur, target):
            if len(cur) == k and target == 0 and cur not in res:
                res.append(cur[:])
                return 

            for i in range(start, 9):
                if len(cur) < k and arr[i] <= target:
                    cur.append(arr[i])
                    backtrack(i + 1, cur, target - arr[i])
                    cur.pop()
                    backtrack(i + 1, cur, target)
                    
        backtrack(0, [], n)
        return res

