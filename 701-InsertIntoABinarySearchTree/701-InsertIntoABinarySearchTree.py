# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        """
        learning on neetcode rn

        will be back.


        0 ms runtime beats 100%
        """
        
        if not root:
            return TreeNode(val)    # return a treenode obj when root doesnt exist, so for example when im going to root.right, it doesnt exist, i just set it to this treenode i js made since root.right = self.insertIntoBST(root.right, val)

        if val > root.val: # go right
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val: # go left
            root.left = self.insertIntoBST(root.left, val)
        
        return root

