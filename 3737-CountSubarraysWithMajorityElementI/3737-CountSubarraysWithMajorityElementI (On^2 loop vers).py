class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:

        """
        oooooouuuu shiii loop version O(n^2) works quickerrrrr

        1629 ms runtime beats 60%
        """
        
        res = 0
        n = len(nums)

        for start in range(n):
            amt_target = 0
            arr_len = 0
            for i in range(start, n):
                if nums[i] == target:
                    amt_target += 1

                arr_len += 1

                if amt_target > arr_len // 2:
                    res += 1

        return res
