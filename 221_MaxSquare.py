  # Given a 2D binary matrix filled with 0's and 1's, find the largest square cont
# aining only 1's and return its area. 
# 
#  Example: 
# 
#  
# Input: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Output: 4
#  Related Topics Dynamic Programming 
#  👍 3463 👎 89


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        maxSide = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) +1
                    maxSide = max(maxSide, dp[i][j])
        return maxSide ** 2

考虑矩阵右下角的1，检查他周围的上，左，左上的1

# leetcode submit region end(Prohibit modification and deletion)
