class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zeros = []

        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    zeros.append((x,y))

        for zero_x, zero_y in zeros:
            for x in range(m):
                matrix[x][zero_y] = 0
            for y in range(n):
                matrix[zero_x][y] = 0
    # O(mn) time complexity, O(m+n) space complexity

    def other_solution(self, matrix: list[list[int]]) -> None:
        """
        Use first row and first column as a flag to store the information of zeros.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row = False
        first_col = False

        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    if x == 0:
                        first_row = True
                    if y == 0:
                        first_col = True
                    matrix[x][0] = 0
                    matrix[0][y] = 0

        for x in range(1, m):
            if matrix[x][0] == 0:
                for y in range(1, n):
                    matrix[x][y] = 0

        for y in range(1, n):
            if matrix[0][y] == 0:
                for x in range(1, m):
                    matrix[x][y] = 0

        if first_row:
            for y in range(n):
                matrix[0][y] = 0

        if first_col:
            for x in range(m):
                matrix[x][0] = 0
    # O(mn) time complexity, O(1) space complexity
