class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        """
        this one actually fried my brain im so dumb

        had to look at the solutions, will do sliding window next.

        what happened:
        originally tried with a brute-force approach and thought i was smart and i thought it was sliding window but it wasnt.
        it was actually a O(n^2) solution but it was at 4 am so i was fried already.
        tried to use set first and then didnt work so moved to dict and still had difficulties due to tle. will try to recover that tle solution for github as well.

        61 ms runtime beats 90%
        """
        
        res = 0
        n = len(s)
        m = [-1,-1,-1]  # for last seen index in order 'a' 'b' 'c'

        for i in range(n):
            
            m[ord(s[i]) - ord('a')] = i # sets last seen index for whatever char this is

            start = min(m)

            if start != -1:
                res += start + 1

        return res
                
