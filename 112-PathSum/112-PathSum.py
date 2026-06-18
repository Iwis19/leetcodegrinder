# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        """
        YUSSSSSS    

        still giving myself ti me to improve at bst + recursion + dfs algos, went pretty good since i had a general idea this time !!!

        0 ms runtime beats 100%
        """
        
        def dfs(root, target):
            
            # if the target still isnt met and the node doesnt even exist, then its a false
            if not root:
                return False

            remaining = target - root.val

            if remaining == 0 and not root.left and not root.right:
                return True

            return dfs(root.left, remaining) or dfs(root.right, remaining)

        return dfs(root, targetSum)
