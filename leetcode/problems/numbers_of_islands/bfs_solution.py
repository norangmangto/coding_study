class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0: return 0

        no_of_islands = 0
        max_size = 0
        for i in range(len(grid)):  # column
            for j in range(len(grid[i])):  # row
                size = self.bfs(grid, i, j)
                if size > 0:
                    no_of_islands += 1
                    if max_size < size:
                        max_size = size

        return no_of_islands

    def bfs(self, grid, i, j):
        size = 0
        queue = [(i, j)]
        while queue:
            x, y = queue.pop(0)
            if grid[x][y] == '1':
                size += 1
                grid[x][y] = '0'
                if y-1 >= 0: queue.append((x, y-1))  # left
                if y+1 < len(grid[x]): queue.append((x, y+1))  # right
                if x-1 >= 0: queue.append((x-1, y))  # up
                if x+1 < len(grid): queue.append((x+1, y))  # down

        return size
