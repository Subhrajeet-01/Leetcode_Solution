class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        memo = {}
        def dfs(i, j):
            if i == m-1 and j == n-1:
                return grid[i][j]    
            
            if (i, j) in memo:
                return memo[(i, j)]
            min_sum = float('inf')
            if i + 1 < m:
                min_sum = min(min_sum, dfs(i + 1, j))
            if j + 1 < n:
                min_sum = min(min_sum, dfs(i, j + 1))

            memo[(i, j)] = grid[i][j] + min_sum
            return memo[(i, j)]
        
        return dfs(0, 0)