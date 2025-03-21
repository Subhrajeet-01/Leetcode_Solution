# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        self.inorder(root, ans)
        return ans[k-1]
    def inorder(self, root, ans):
        if not root:
            return 

        self.inorder(root.left, ans)
        ans.append(root.val)
        self.inorder(root.right, ans)

