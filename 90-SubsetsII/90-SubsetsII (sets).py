class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        """
        set brute force (bad tc)

        0 ms runtime beaats 100% tho
        """
        
        nums.sort()
        res = []
        n = len(nums)
        visited = set()

        def dfs(start, prev_arr):

            res.append(prev_arr[:])
            visited.add(tuple(prev_arr[:]))
                
            for i in range(start, n):
                prev_arr.append(nums[i])

                if tuple(prev_arr[:]) in visited:
                    prev_arr.pop()
                    continue

                dfs(i+1, prev_arr)
                prev_arr.pop()

        dfs(0, [])

        return res
