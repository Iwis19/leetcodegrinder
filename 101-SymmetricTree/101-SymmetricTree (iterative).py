# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        """
        needed a bit of help from chat jipiti, but i guess mostly right ideas. should def use None more isntead of some bs palceholder like "" that i use rn

        0 ms runtime beats 100%
        """

        q = deque()
        q.append(root)

        while q:

            vals = []

            for _ in range(len(q)):
                node = q.popleft()

                if not node:
                    vals.append(None)
                    continue

                vals.append(node.val)
                
                q.append(node.left)
                q.append(node.right)

            if vals != vals[::-1]:
                return False
            
        return True




