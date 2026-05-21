class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        """
        dummy mode solution i actually dont understand partition + binary search

        will come back to understand the partitions in a few months.

        0 ms runtime beats 100%
        """

        m, n = len(nums1), len(nums2)

        new = []
        i, j = 0, 0

        while i < m and j < n:

            if nums1[i] <= nums2[j]:
                new.append(nums1[i])
                i += 1
            else:
                new.append(nums2[j])
                j += 1

        while i < m:
            new.append(nums1[i])
            i += 1

        while j < n:
            new.append(nums2[j])
            j += 1

        mid = (m+n) // 2
        if (m+n) % 2 == 1:
            return new[mid]
        else:
            return (new[mid-1] + new[mid]) / 2

        return 


        
