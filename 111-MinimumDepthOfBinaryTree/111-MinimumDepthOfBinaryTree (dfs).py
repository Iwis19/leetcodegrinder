# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        """
        straight death i still dont very much get it recursion is too hard

        61 ms runtime beats 12%
        """
        
        if not root:
            return 0

        left, right = self.minDepth(root.left), self.minDepth(root.right)
        if not left:
            return 1 + right

        if not right:
            return 1 + left

        return 1 + min(left, right)
