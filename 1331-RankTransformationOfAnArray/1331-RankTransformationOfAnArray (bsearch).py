class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        """
        BRO FUCK I FUCKED UP BSEARCH HOW IN THE WORELD

        246 ms just for fun
        """

        if not arr:
            return []

        n = len(arr)
        temp_dupes = sorted(arr)
        temp = [temp_dupes[0]]

        for i in range(1, n):
            if temp_dupes[i] != temp_dupes[i-1]:
                temp.append(temp_dupes[i])

        def binary_search(num: int) -> int:
            l,r = 0, len(temp) - 1
            

            while l <= r:
                m = (l+r)//2
                if num == temp[m]:
                    return m + 1   # return the ranking
                elif num < temp[m]:
                    r = m-1
                else:
                    l = m+1

            return 1

        for i in range(n):
            arr[i] = binary_search(arr[i])

        return arr
