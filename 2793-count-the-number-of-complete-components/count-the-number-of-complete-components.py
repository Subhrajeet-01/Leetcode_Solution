class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        complete_count = 0
        
        def dfs(node, node_data):
            visited.add(node)
            node_data[0] += 1
            node_data[1] += len(graph[node])
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, node_data)
            
        for node in range(n):
            if node not in visited:
                node_data = [0, 0]
                dfs(node, node_data)
                count, degree_sum = node_data
                if degree_sum == count * (count - 1):
                    complete_count += 1
        
        return complete_count