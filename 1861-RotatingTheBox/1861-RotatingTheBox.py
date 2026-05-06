class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        
        """
        deadass spent an hour and 30 minutes on this daily. didnt even pass. needed external help to figure out what went wrong

        1. initially started with a while loop to scan from backwards and created conditionals to move stones back when space is spotted
        2. eventually noted that i needed a two pointer approach since when there are scenarios like [# . . # . #], my stones do not get moved as back as 
        possible.
        3. moved onto two pointer, struggled to do so, had to scrap while loop idea and consider conditionals.
        4. peeked at hint without knowing it was going to help with matrix rotation, mostly figured out rotation logic by myself

        147 ms runtime beats 36% O(m*n) optimized time complexity
        """


        
        # move for gravity before i rotate

        m, n = len(boxGrid), len(boxGrid[0])

        for row in range(m):

            empty = n-1

            for i in range(n-1, -1, -1):

                if boxGrid[row][i] == ".":
                    continue

                elif boxGrid[row][i] == "*":
                    empty = i - 1

                elif boxGrid[row][i] == "#":
                    boxGrid[row][i] = "."
                    boxGrid[row][empty] = "#"
                    empty -= 1


        # rotate now

        res = [['' for _ in range(m)] for _ in range(n)]

        for i in range(m):

            for j in range(n):

                res[j][m-i-1] = boxGrid[i][j]
                
        return res
                
                


