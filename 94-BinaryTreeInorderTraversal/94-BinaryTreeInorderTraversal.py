# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        """
        starting to learn binary trees, need to keep inorder, preorder, postorder methods in mind.

        inorder: parent node is BETWEEN left and right
        preorder: parent node is BEFORE left and right
        postorder: parent node is AFTER left and right

        0 ms runtime beats 100%
        """
        
        res = []

        def inorder(root):

            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res
            
