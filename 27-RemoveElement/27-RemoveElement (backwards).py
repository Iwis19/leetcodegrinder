class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        """
        i spent like 1.5 hour on this i actrually hate myself im genuinely so dumb
        
        0 ms runtime beats 100%
        """
        
        n = len(nums)
        good_i = -1

        # (backwards) first good swappable number (nums[good_i] != val)
        for i in range(n-1, -1, -1):
            if nums[i] != val:
                good_i = i
                break

        for i in range(n):

            if good_i <= i:
                break

            # good, no need to swap
            if nums[i] != val:
                continue
            
            # else, we are going to swap this bad numbner with a nums[good_i]
            nums[i], nums[good_i] = nums[good_i], nums[i]

            # finds next nearest (backwards) number that != val
            while good_i >= 0 and nums[good_i] == val:
                good_i -= 1
 
        return good_i + 1
