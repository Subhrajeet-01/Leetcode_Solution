# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def match_parent(self, root, parent_map):
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.left:
                parent_map[node.left] = node
                queue.append(node.left)
            
            if node.right:
                parent_map[node.right] = node
                queue.append(node.right)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_map = {}
        self.match_parent(root, parent_map)

        queue = deque([target])
        seen = {target}
        cur_distance = 0

        while queue:
            if cur_distance == k:
                break
            cur_distance += 1
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left and node.left not in seen:
                    seen.add(node.left)
                    queue.append(node.left)
                if node.right and node.right not in seen:
                    seen.add(node.right)
                    queue.append(node.right)
                if node in parent_map and parent_map[node] not in seen:
                    seen.add(parent_map[node])
                    queue.append((parent_map[node]))

        return [node.val for node in queue]