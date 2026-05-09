class Solution:
    def isPalindrome(self, s: str) -> bool:

        """
        7 ms runtime beats 81%
        """
        
        clean = []
        for char in s:
            if char.isalnum():
                clean.append(char.lower())

        clean_s = "".join(clean)

        return clean_s == clean_s[::-1]
