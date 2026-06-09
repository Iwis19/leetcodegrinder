class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:

        """
        very very quick question. spotted the main idea

        had a pretty butt runtime though because for some reason i went with max(num for num in nums) when i couldve just went
        for max(nums), no difference. learned to only use the first one when i wanna modify the values.

        9 ms runtime beats 75% same as optimal solution O(n)
        """
        
        return k * (max(nums) - min(nums))
