class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        """
        this is unaccceptable i hate my brain imd umb as hell really need to get back on the lc grind next month

        3 ms runtime beats 83%
        """

        rows, cols = len(grid), len(grid[0])
        if not k: return grid
        if k % (rows * cols) == 0: return grid

        arr = [ [0] * cols for _ in range(rows) ]
        
        for r in range(rows):
            for c in range(cols):

                new_i = (r * cols + c + k) % (rows * cols)

                new_r = new_i // cols
                new_c = new_i % cols

                arr[new_r][new_c] = grid[r][c]

        return arr
