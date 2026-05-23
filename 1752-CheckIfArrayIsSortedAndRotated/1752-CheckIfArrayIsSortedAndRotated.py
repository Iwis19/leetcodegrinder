class Solution:
    def check(self, nums: List[int]) -> bool:

        """
        im faking stupid i put nums[1] instead of nums[0]

        0 ms runtime beats 100%
        """
        
        # keep a check for the peak and then /....

        peak = False 
        n = len(nums)

        if n == 1:
            return True

        for i in range(1, n):
            # if curr > prev, only fine if peak = False, else we return not sorted alr
            if nums[i] < nums[i-1]:
                if not peak:
                    peak = True
                    continue
                else:
                    return False

        # if peak = True, we check if FIRST > LAST
        
        if not peak and nums[0] > nums[-1]:
            return False

        if peak and nums[0] < nums[-1]:
            return False

        return True
            

