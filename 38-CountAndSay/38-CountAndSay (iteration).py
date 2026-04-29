class Solution:
    def countAndSay(self, n: int) -> str:

        """
        iterative way

        7 ms runtime beats 77% 
        """

        def rle(string: str) -> int:
            count = 1
            res = ""

            for i in range(1, len(string)):
                if string[i] != string[i-1]:
                    res += f"{count}{string[i-1]}"
                    count = 1

                elif string[i] == string[i-1]:
                    count += 1
                
            res += f"{count}{string[-1]}"
            
            return res


        result = "1"
        # since we already have base case, its just start of 1
        for i in range(1, n):
            result = rle(result)
        return result
    
        

        
