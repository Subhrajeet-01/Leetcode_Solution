# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []
        if root is None:
            return postorder
        stack1, stack2 = [], []
        stack1.append(root)

        while stack1:
            root = stack1.pop()
            stack2.append(root)
            if root.left is not None:
                stack1.append(root.left)
            if root.right is not None:
                stack1.append(root.right)
            # print("root = ", root)
            # print("stack2 = ", stack2)
            # print("stack1 = ", stack1)
        
        while stack2:
            postorder.append(stack2[-1].val)
            stack2.pop()

        return postorder