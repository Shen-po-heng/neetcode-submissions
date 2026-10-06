class Solution:
    def dfs(self,r, c,rows,cols,visited,grid):
        if (
            r < 0 or r >= rows or
            c < 0 or c >= cols or
            grid[r][c] == "0" or
            (r, c) in visited
        ):
            return

        if (r, c) in visited:
            return

        visited.add((r, c))

        self.dfs(r + 1, c,rows,cols,visited,grid)
        self.dfs(r - 1, c,rows,cols,visited,grid)
        self.dfs(r, c + 1,rows,cols,visited,grid)
        self.dfs(r, c - 1,rows,cols,visited,grid)
        return 1

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        num_island = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    self.dfs(r, c,rows,cols,visited,grid)
                    num_island += 1
        return num_island
                