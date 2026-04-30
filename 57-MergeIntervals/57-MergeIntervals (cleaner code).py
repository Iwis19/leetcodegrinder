class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        """
        learned that sort sorts lexicographically (starts from the first val, and then move onto next val, as well as for strs)

        i spent time debugging, but i actually identified the issue myself and looked for a fix (mostly knew how to do)

        also did case counting by myself, just that it took a few submissiosn to realize

        mostly need to learn to write cleaner code though definitely

        yay optimal solution 7 ms runtime beats 72%
        """
        
        intervals.sort()

        res = []
        l = len(intervals)

        if l == 1:
            return intervals
        
        for i in range(l):

            curr = intervals[i]

            if not res or (res[-1][1] < curr[0]):  #only works bc not res will return true when it IS EMPTY, so the rest wont run as python can alr decide on a result
                res.append(curr)
            else:
                prev = res[-1]
                res[-1][1] = max(curr[1], prev[1])

            # 3 cases: entirely does not overlap, entirely overlaps, partially overlaps  

        return res

