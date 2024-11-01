class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        old_color = image[sr][sc]

        if color == old_color:
            return image

        def dfs(r, c):
            if not 0 <= r < ROWS or not 0 <= c < COLS:
                return
            
            if image[r][c] == old_color:
                image[r][c] = color
                
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
        dfs(sr, sc)

        return image