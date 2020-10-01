# Given a 2d grid map of '1's (land) and '0's (water), count the number of islan
# ds. An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are all su
# rrounded by water. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#  
#  Related Topics Depth-first Search Breadth-first Search Union Find 
#  👍 6499 👎 210


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        # n = len(grid[0])

        def dfs(grid, x, y):
            if not 0 <= x < m or not 0 <= y < len(grid[0]) or grid[x][y] == '0': return
            grid[x][y] = '0'  # 要把已经处理过了的点标记为0，以免之后重复搜索这一个点
            for nx, ny in [[x + 1, y], [x - 1, y], [x, y - 1], [x, y + 1]]:
                dfs(grid, nx, ny)

        count = 0

        for i in range(m):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count

# leetcode submit region end(Prohibit modification and deletion)
