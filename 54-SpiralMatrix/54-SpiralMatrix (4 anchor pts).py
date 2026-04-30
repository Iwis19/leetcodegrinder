class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        """
        did this a while ago, but wasnt checked off so i decided to redo it

        honestly was a big challenge still, esp with indexing ideas: 
        - tried m,n and m-1,n-1, basically inclusive or exclusive cases options, so i tried out both and decided to stick to one
        
        used lots of time to debug, which was good practice, enjoyed the process

        will come back again some day

        0 ms runtime beats 100
        """
        
        res = []

        m = len(matrix)
        n = len(matrix[0])

        top, left = 0, 0
        bottom, right = m, n   # for inclusive rather than exclusive


        """
        123 top 1, left 0, bottom 3, right 3
        69 top 1, left 0, bottom 3, right 2
        87 top 1, left 0, bottom 2, right 2
        4 top 1, left 1, bottom 2, right 2
        5 top 2, left 1, bottom 2, right 2


        """

        while bottom > top and right > left:
            
            # top row move right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            # right column move down
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1

            # bottom row move left
            if bottom > top:
                for i in range(right-1, left-1, -1):
                    res.append(matrix[bottom-1][i])
                bottom -= 1

            # left column move up
            if right > left:
                for i in range(bottom-1, top-1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res
