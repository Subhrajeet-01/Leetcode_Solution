class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        Row, Column = len(isWater), len(isWater[0])
        q = deque()
        res = [[-1] * Column for _ in range(Row)]
        
        # Multiple Source BFS
        for r in range(Row):
            for c in range(Column):
                if isWater[r][c]:
                    q.append((r, c))
                    res[r][c] = 0
        
        while q:
            r, c = q.popleft()
            h = res[r][c]
            neighbors = [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]
            for nr, nc in neighbors:
                if (nr < 0 or nc < 0 or nr == Row or nc == Column or res[nr][nc] != -1):
                    continue
                q.append((nr, nc))
                res[nr][nc] = h + 1
        return res