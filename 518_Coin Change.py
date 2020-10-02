# You are given coins of different denominations and a total amount of money. Wr
# ite a function to compute the number of combinations that make up that amount. Y
# ou may assume that you have infinite number of each kind of coin. 
# 
#  
#  
# 
#  
# 
#  Example 1: 
# 
#  
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#  
# 
#  Example 2: 
# 
#  
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
#  
# 
#  Example 3: 
# 
#  
# Input: amount = 10, coins = [10] 
# Output: 1
#  
# 
#  
# 
#  Note: 
# 
#  You can assume that 
# 
#  
#  0 <= amount <= 5000 
#  1 <= coin <= 5000 
#  the number of coins is less than 500 
#  the answer is guaranteed to fit into signed 32-bit integer 
#  
#  👍 2331 👎 67


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
# dp[0][0] = 1
# dp[0][i] = 0
# dp[i][j] = dp[i-1][j] + dp[i][j-coin[i]]
# 前i种硬币构造出钱总数为j的组合数
# 只需要一维的数组就行了

        dp = [1] + [0] * amount
        for c in coins:
            for i in range(c, amount+1):
                dp[i] += dp[i-c]
        return dp[amount]


# leetcode submit region end(Prohibit modification and deletion)
