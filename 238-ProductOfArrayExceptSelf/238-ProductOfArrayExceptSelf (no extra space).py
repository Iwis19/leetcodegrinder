class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # prefix and suffix

        # so im apparently supposed to update my result arr as i go on to update my prefix and suffix sums

        """
        21 ms runtime beats 62% no extra space
        """

        n = len(nums)
        res = [1] * n

        prefix, suffix = 1, 1

        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]

        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res


        
