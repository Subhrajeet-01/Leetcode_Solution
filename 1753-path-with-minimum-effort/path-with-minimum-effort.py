class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        vis = set()
        direction = [[0, 1],[0, -1],[1, 0], [-1, 0]]
        minHeap = [[0, 0, 0]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r, c) in vis:
                continue
            vis.add((r, c))
            if (r, c) == (row - 1, col - 1):
                return diff
            
            for dr, dc in direction:
                newR, newC = r + dr, c + dc
                if (newR < 0 or newC < 0 or newR == row or newC == col or (newR, newC) in vis):
                    continue
                
                newDiff = max(diff, abs(heights[r][c] - heights[newR][newC]))
                heapq.heappush(minHeap, [newDiff, newR, newC])