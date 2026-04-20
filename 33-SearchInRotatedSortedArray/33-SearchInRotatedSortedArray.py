class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1


        """
        example: arr = [0,1,2,3,4]

        notice that one half is always going to be sorted:
        rotated left 1: [4,0,1,2,3] -> 1,2,3 (right)
        rotated left 2: [3,4,0,1,2] -> 0,1,2 (right)
        rotated left 3: [2,3,4,0,1] -> 2,3,4 (left)
        rotated left 4: [1,2,3,4,0] -> 1,2,3 (left)
        rotated left 5: [0,1,2,3,4] -> 2,3,4 (right)

        1. i actually needed a lot of help on this since i didnt really see the possibility of binary search here and the 
        if statements still feel kind of iffy to me

        0 ms runtime beats 100
        """

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # left is sorted
            if nums[left] <= nums[mid]:
                # if the target is within the left half
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                # if the target is within the right half
                else:
                    left = mid+1

            # right is sorted
            else:
                # if the target is within the right half
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                # if the target is within the left half
                else:
                    right = mid-1

        return -1
        
