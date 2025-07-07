class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def helper(grid, i, j, m, n):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j] == '0':
                return

            grid[i][j]='0'
            helper(grid, i+1 ,j, m, n)
            helper(grid, i-1, j, m, n)
            helper(grid, i, j-1, m, n)
            helper(grid, i, j+1, m, n)

        ans = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j]=='1':
                    helper(grid, i, j, m, n)
                    ans+=1

        return ans