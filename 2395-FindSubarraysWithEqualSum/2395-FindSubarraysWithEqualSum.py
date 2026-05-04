class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:

        map = {}

        for i in range(len(nums)-1):
            sum = nums[i] + nums[i+1]
            if sum not in map:
                map[sum] = 0
            map[sum] += 1

        for val in map.values():
            if val != 1:
                return True

        return False
        
