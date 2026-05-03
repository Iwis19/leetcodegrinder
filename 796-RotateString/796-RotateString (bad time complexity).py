class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        def shift(s: str):

            arr = ['' for _ in range(len(s))]
            arr[0] = s[-1]
            for i in range(len(s)-1):
                arr[i+1] = s[i]

            return "".join(arr)

        shifted = s 
        for _ in range(len(s)):
            shifted = shift(shifted)
            if shifted == goal:
                return True

        return False
