# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        """
        some things i  learned from this (not so) easy easy problem 

        for binary trees, there are only 2  ways of solving: bfs, dfs.
        
        for bfs, there are ways of outputting hte results / info that i need or i need to calculate
        for dfs, you often either:
            - use the given function to use as a recursion method
            - code a helper method inside given function to do recursion, and then work on an output, then use the main function to do decide on final
            results based on hte output from helper method

        but for dfs, it is often harder for me since even though i understand the very basic dfs algo, i dont knjow how to switch it up.

        4 ms runtime beats 30% but same as 0 ms solution
        """

        def dfs(root):
            if not root:
                return 0

            l, r = dfs(root.left), dfs(root.right)

            if l == -1 or r == -1 or abs(l-r) > 1:
                return -1

            return 1 + max(l, r)

        return dfs(root) != -1
            
        
        




        
