# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 0
        arr = self.dfs(root, [])
        arr.sort()
        return arr[k-1]

    def dfs(self, root, ans):
        ans.append(root.val)
        if root.left:
            self.dfs(root.left, ans)
        if root.right:
            self.dfs(root.right, ans)
        return ans
        