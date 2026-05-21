class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        """
        damn needed hint 1 

        but good implementation and debuging practices!

        7 ms runtime beats 67% O(n) optimized
        """
        
        n = len(A)
        freq = [[] for _ in range(n+1)] # 0 indexed arr, so we get 1 more length to be able to store 1,2,3,4 when n = 4

        res = [0] * n

        for i in range(n):
            freq[A[i]].append(i)
            freq[B[i]].append(i)

        for i in range(1, n+1):
            index = freq[i][1]
            res[index] += 1

        for i in range(1, n):
            res[i] += res[i-1]

        return res


