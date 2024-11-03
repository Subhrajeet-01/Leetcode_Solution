class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        def dfs(i, j):
            visited[i][j] = 1
            dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            for a,b in dir:
                row = a + i
                col = b + j
                if row >= 0 and row < n and col >= 0 and col < m and board[row][col] == 'O' and not visited[row][col]:
                    dfs(row, col)
        
        visited = [[0 for _ in range(m)] for i in range(n)]
        for j in range(m):
            if not visited[0][j] and board[0][j] == 'O':
                dfs(0 , j)
            if not visited[n-1][j] and board[n-1][j] == 'O':
                dfs(n-1 , j)
        
        for i in range(n):
            if not visited[i][0] and board[i][0] == 'O':
                dfs(i, 0)
            if not visited[i][m-1] and board[i][m-1] == 'O':
                dfs(i, m-1)
        
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and board[i][j] == 'O':
                    board[i][j] = 'X'
        
        return board
    