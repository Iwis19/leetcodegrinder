class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        """
        more optimized version of brute force

        had the right idea for dp but didnt realize prefix

        267 ms runtime beats 72%
        """
        
        def check(n: int) -> int:

            string = str(n)
            l = len(string)
            count = 0

            if l < 3:
                return count

            for i in range(1, l-1):
                if string[i-1] > string[i] < string[i+1] or string[i-1] < string[i] > string[i+1]:
                    count += 1

            return count

        res = 0

        for num in range(num1, num2+1):
            res += check(num)

        return res
