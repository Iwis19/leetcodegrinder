# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxNode(self, root) -> TreeNode:
        # always go right
        if not root:
            return None
        while root.right:
            root = root.right
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None

        if root.val < key:  # go right
            root.right = self.deleteNode(root.right, key)

        elif root.val > key: # go left
            root.left = self.deleteNode(root.left, key)

        else:

            if not root.left:          # if theres no left branch, we just connect the right (could be None) branch to the parent node
                return root.right
            elif not root.right:       # if there is no right branch, we just connect left branch to parent node
                return root.left    
            else:
                max = self.maxNode(root.left)    # if theres 2 children, we copy the maxnode of parent's left subtree to use as the new parent, and then delete the maxnode from left tree, this is because maxnode of parents left OR minnode of parents right would be a good sub for parent node's removal.
                root.val = max.val
                root.left = self.deleteNode(root.left, max.val)   # later delete the "duplicate" children node

        return root   # since root is not modified, return root for final check
