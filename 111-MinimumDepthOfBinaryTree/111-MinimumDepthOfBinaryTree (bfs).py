# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:


        """
        for this bfs solution, i dont need the for loop anymore to keep track of each level. im already storing all of that
        in the 2nd element of the arr that stores the node, so im already keeping track of it anyways.

        this one makes more sense than recursion. idk how to get good at recursion its hard.

        0 ms runtime beats 100%
        """


        if not root:
            return 0
        
        depth = 1

        q = deque([[root, 1]])

        while q:

            node, depth = q.popleft()

            if node.left:
                q.append([node.left, depth + 1])

            if node.right:
                q.append([node.right, depth + 1])

            if not node.right and not node.left:
                return depth

        return depth
