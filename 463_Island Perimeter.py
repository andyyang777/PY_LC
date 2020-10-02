# You are given row x col grid representing a map where grid[i][j] = 1 represent
# s land and grid[i][j] = 0 represents water. 
# 
#  Grid cells are connected horizontally/vertically (not diagonally). The grid i
# s completely surrounded by water, and there is exactly one island (i.e., one or 
# more connected land cells). 
# 
#  The island doesn't have "lakes", meaning the water inside isn't connected to 
# the water around the island. One cell is a square with side length 1. The grid i
# s rectangular, width and height don't exceed 100. Determine the perimeter of the
#  island. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [[1]]
# Output: 4
#  
# 
#  Example 3: 
# 
#  
# Input: grid = [[1,0]]
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  row == grid.length 
#  col == grid[i].length 
#  1 <= row, col <= 100 
#  grid[i][j] is 0 or 1. 
#  
#  Related Topics Hash Table 
#  👍 2279 👎 126


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 可以考虑为，一开始都初始化默认每个格子都是4，然后两个只要相邻，那么就减2，
    # 然后只需要考虑左边和上边的情况，因为格子的右和下，其实是它自己右边那个和下边那个格子的左和上
    # 所以只需要考虑格子的左和上的情况
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4
                    if i>0 and grid[i-1][j] == 1: # 上面是1,而且i>0因为0行的上面肯定没有，同理下面的j，因为0列的左边肯定没有
                        res -= 2
                    if j>0 and grid[i][j-1] == 1: # 左边有1
                        res -= 2
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
