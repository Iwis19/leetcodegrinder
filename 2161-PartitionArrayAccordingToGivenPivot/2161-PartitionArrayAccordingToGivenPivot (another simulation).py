class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        """
        ok so i was trying to code out my solution as seen in the comments below but i thought it wasnt so smooth so i checked the answers. im not very sure if this even ccounts as two pointer since its mostly just simulation all over again, but i guess?
        my approach was very off from this though. the original 2 ptr idea was below, so go rread it

        okay 51 ms runtime beats 20%
        """

        n = len(nums)
        res = [pivot] * n

        greater, smaller = 0, 0

        for num in nums:
            if num > pivot:
                greater += 1
            elif num < pivot:
                smaller += 1

        greater_pos, smaller_pos = n - greater, 0

        for num in nums:
            if num > pivot:
                res[greater_pos] = num
                greater_pos += 1
            elif num < pivot:
                res[smaller_pos] = num
                smaller_pos += 1

        return res


        # ptr = -1
        # cnt = 0

        # # first pivot location + amt of pivots
        # for i in range(n):
        #     if ptr == -1 and nums[i] = pivot:
        #         ptr = i
        #     cnt += 1

        # for i in range(n):

        #     """
        #     1. smaller than pivot: move to right before pivot
        #     2. equal to pivot: move to right after the current pivot
        #     3. larger than pivot: move to the very end
        #     """


        
        
