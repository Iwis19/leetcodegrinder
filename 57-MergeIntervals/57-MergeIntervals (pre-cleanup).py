class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        intervals.sort()

        res = []
        l = len(intervals)

        if l == 1:
            return intervals
        
        for i in range(l):
            curr = intervals[i]
            if not res:
                res.append(curr)
                continue
            prev = res[-1]

            # 3 cases: entirely does not overlap, entirely overlaps, partially overlaps
            # entirely overlaps
            if prev[1] >= curr[1]:
                continue
            # partially overlaps
            if prev[1] >= curr[0]:
                res[-1][1] = curr[1]
                continue
            # no overlap
            res.append(curr)    

        return res


intervals = [[1,4],[0,2],[3,5]]
ans = Solution().merge(intervals) 
print(ans)

