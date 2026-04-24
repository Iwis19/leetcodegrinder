class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        """
        needed some help on prefix sum, i didnt know this was a thing, but it was a solution i shouldve thought abt

        139 ms beats 59% optimized O(N)
        """
        
        n = len(nums)
        res = [0] * n
        map = {}

        for i in range(n):
            num = nums[i]
            if num not in map:
                map[num] = []
            map[num].append(i)

        for arr in map.values():
            m = len(arr)
            total = sum(arr)
            left_sum = 0
            
            """
            for each number in this array, we find its left sum and right sum of indices

            right_sum = total indices sum - current index - left indices sum
            left_sum += current index

            calculate the left contribution and right

            and keep updating
            """
            for i in range(m):
                right_sum = total - arr[i] - left_sum

                left = arr[i] * i - left_sum

                """
                i(n) - arr[i] + i(n+1) - arr[i] + i(n+2) - arr[i]

                rightsum - arr[i]*(m-i-1)
                """
                right = right_sum - arr[i] * (m-i-1)

                res[arr[i]] = right + left
                left_sum += arr[i]

        return res

            
                
                
