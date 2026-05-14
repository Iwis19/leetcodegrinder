class Solution:
    def isGood(self, nums: List[int]) -> bool:

        n = len(nums)

        # makes like [0, 0, 0, 0] -> for number 0, 1, 2, 3
        freq = [0] * (n) # for example for [1,2,3,3], we have n = 4, but we should have 3 distinct numbers, where the val of last index should be 2.

        for num in nums:
            if num >= n:
                return False

            freq[num] += 1

        for i in range(1, n-1):
            if freq[i] != 1:
                return False

        return freq[-1] == 2
