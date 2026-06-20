class Solution:
    def combinationSum2(self, c: List[int], t: int) -> List[List[int]]:

        """
        took me like 45 mins. but we did itttttttttt i debugged for 40 mins out of the 45

        7 ms runtime beats 63% WOOOHOO
        """
        
        c.sort() #[1,1,2,5,6,7,10]  #[1,2,2,2,5]

        res = []
        seen = set()
        n = len(c)

        # arr = [0]   # indices of distinct values in c
        # for i in range(1, n):
        #     if c[i] != c[i-1]:
        #         arr.append(i)

        def dfs(start, target, curr):

            copy = curr[:]
            
            if tuple(copy) in seen:
                return

            seen.add(tuple(copy))

            if target == 0:
                res.append(copy)
                return

            for i in range(start, n):
                
                remaining = target - c[i]

                if remaining < 0:
                    return 

                curr.append(c[i])
                dfs(i+1, remaining, curr)
                curr.pop()

        for i in range(n):
            dfs(i, t, [])
        
        return res
