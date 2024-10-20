# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        q = deque()
        q.append(root)
        zigzag = True
        while q:
            size = len(q)
            level = []
            for i in range(size):
                node = q.popleft()
                level.append(node.val)

                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if zigzag:
                ans.append(level)
                zigzag = not zigzag
            else:
                ans.append(level[::-1])
                zigzag = not zigzag
            
        return ans