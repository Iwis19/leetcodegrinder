class Solution:
    def findGCD(self, nums: List[int]) -> int:
        """
        loooowkey just memorzed gcd algorithm because ive done it like 2 days ago so its gotta stickkkkkkkkkk

        euclidean algo for gcd: 
        
        gcd(a,b) = gcd(b, a%b)
        a, b = 36, 24

        36, 24, r = 12
        24, 12, r = 0
        return b = 12 -> gcd!!! 

        *regardless of a>b or b>a it will work regardless

        0 ms runtime beats 100%
        """

        mini, maxi = math.inf, -math.inf

        for num in nums:
            if num < mini:
                mini = num
            if num > maxi:
                maxi = num

        while maxi != 0:
            mini, maxi = maxi, mini % maxi

        return mini
