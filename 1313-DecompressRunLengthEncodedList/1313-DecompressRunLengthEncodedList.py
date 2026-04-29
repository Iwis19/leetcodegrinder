class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:

        """
        0 ms runtime beats 100
        """

        res = []
        
        for i in range(0,len(nums),2):

            count = nums[i]
            number = nums[i+1]
            
            for _ in range(count):
                res.append(number)

        return res

