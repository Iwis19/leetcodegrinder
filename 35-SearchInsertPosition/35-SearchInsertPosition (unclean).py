class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        """
        highkey figured it out on my own but it was so nasty like it looks like junk code

        0 ms runtime beats 100
        """
        
        # probably a binary search variation

        l,r = 0, len(nums)-1
        if target <= nums[0]: return 0
        if target > nums[-1]: return len(nums)
        if target == nums[-1]: return len(nums)-1

        while l <= r:

            mid = (l+r)//2
            
            if target == nums[mid]:
                return mid
            if l+1 == mid and nums[l] < target < nums[mid]:
                return mid
            if mid+1 == r and nums[mid] < target < nums[r]:
                return r

            if target > nums[mid]: l = mid+1
            elif target < nums[mid]: r = mid-1

        return 0
