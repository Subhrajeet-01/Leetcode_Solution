class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        ans = [[1], [1,1]]
        k = 2
        while numRows > k:
            arr = [1]
            for i in range(k - 1):
                ele = ans[k-1][i] + ans[k-1][i+1]
                arr.append(ele)
            arr.append(1)
            ans.append(arr)
            k += 1
        return ans
            