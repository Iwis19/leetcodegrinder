class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        """
        it made no sense to me but i took a peek at editorial and i could do it. i need to stop doing this and become more confident.

        0 ms runtime beats 100%
        """

        res = []
        
        # l: amt of used left brackets, r: amt of used right brackets
        def dfs(l, r, prev):

            if len(prev) == n * 2:
                res.append(prev)
                return

            if l < n:
                temp = prev + "("
                dfs(l+1, r, temp)
            if r < n and l > r:
                temp = prev + ")"
                dfs(l, r+1, temp)

            return

        dfs(0, 0, "")
        return res
