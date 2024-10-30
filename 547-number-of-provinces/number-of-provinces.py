class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        n = len(isConnected)
        visited = [False] * n
        Queue = deque()

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                count += 1
                Queue.append(i)

                while Queue:
                    node = Queue.popleft()
                    for j in range(n):
                        if isConnected[node][j] and not visited[j]:
                            Queue.append(j)
                            visited[j] = True
            
        return count