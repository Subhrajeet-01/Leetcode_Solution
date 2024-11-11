class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        for i in range(n):
            if color[i] == -1:
                q = deque([i])
                # print(q)
                color[i] = 0
                while q:
                    node = q.popleft()
                    for neibour in graph[node]:
                        # print(node, neibour)
                        if color[neibour] == -1:
                            color[neibour] = 1 - color[node]
                            q.append(neibour)
                            # print("color = ", color)
                            # print("q = ", q)
                        elif color[neibour] == color[node]:
                            return False
        
        return True