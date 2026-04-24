class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        """
        passed yay but i dont think im too happy with the code organization, there probably was a better way to write things out in terms of style

        1. thought about slicing but i realized like it makes a new arr everytime so i didnt want to waste memory allo

        0 ms runtime beats 100
        """
        
        # +1 cuz or else its noninclusive
        for i in range(len(haystack) - len(needle) + 1):

            needle_i = 0
            temp = i

            while needle_i < len(needle):
                if needle[needle_i] == haystack[temp]:
                    temp += 1
                    needle_i += 1
                else:
                    break

            if needle_i == len(needle):
                return i            

        return -1


