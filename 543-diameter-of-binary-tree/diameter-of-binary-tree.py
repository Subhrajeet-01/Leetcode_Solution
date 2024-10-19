# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        self.getLength(root)
        return self.diameter
    
    def getLength(self, root):
        if not root:
            return 0
        left = self.getLength(root.left)
        right = self.getLength(root.right)
        self.diameter = max(self.diameter, left + right)
        return 1 + max(left, right)