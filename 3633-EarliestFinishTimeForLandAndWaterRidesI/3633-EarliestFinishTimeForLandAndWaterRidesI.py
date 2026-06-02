class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:


        # write an arr of end time of land and water, sort it, do 2 binary searches to see which res is smaller

        # 

        """
        how do you even binary search on this bruh

        7 ms runtime beats 88%, originally started with 200+ ms but optimized
        """

        n, m = len(landStartTime), len(waterStartTime)
        
        land_first, water_first = math.inf, math.inf

        min_water_end = min(waterStartTime[i] + waterDuration[i] for i in range(m))
        min_land_end = min(landStartTime[i] + landDuration[i] for i in range(n))

        # land_first
        for i in range(m):

            land_first = min(land_first, max(min_land_end, waterStartTime[i]) + waterDuration[i])

        # water first
        for i in range(n):

            water_first = min(water_first, max(min_water_end, landStartTime[i]) + landDuration[i])

        return min(land_first, water_first)
                
