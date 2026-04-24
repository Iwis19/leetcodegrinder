class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        """
        so confusing
        
        0 ms runtime beats 100
        """

        n = len(nums)

        unique_i, scan_i = 1,1

        # to keep myself away from being confussed, this value is set constant and is assigned right when it is created. so i have to update curr everytime.
        # curr = nums[scan_i]

        while scan_i < n:

            while scan_i < n and nums[scan_i] == nums[scan_i-1]:
                scan_i += 1

            if scan_i >= n:
                break

            nums[unique_i] = nums[scan_i]
            unique_i += 1

            """
            this was so confusing because chatgpt cant explain shit
            
            before i copy the first instance of 2 in the array: 
            nums = [0,1,1,1,1,2,2,3,3,4]
            scan_i = 5
            unique_i = 2

            i copy it:
            nums = [0,1,2,1,1,2,2,3,3,4]
            scan_i = 5
            unique_i = 3

            now, scan_i isnt incremented and is still on 5, so now its going to see 2 != 1 and redo the proces again, until every instance of 1 is swapped to 2 between the unique_i and    
            scan_i. therefore, we need to have scan_i += 1
            """
            scan_i += 1

        return unique_i

        

            

