# You are given coins of different denominations and a total amount of money amo
# unt. Write a function to compute the fewest number of coins that you need to mak
# e up that amount. If that amount of money cannot be made up by any combination o
# f the coins, return -1. 
# 
#  You may assume that you have an infinite number of each kind of coin. 
# 
#  
#  Example 1: 
# 
#  
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#  
# 
#  Example 2: 
# 
#  
# Input: coins = [2], amount = 3
# Output: -1
#  
# 
#  Example 3: 
# 
#  
# Input: coins = [1], amount = 0
# Output: 0
#  
# 
#  Example 4: 
# 
#  
# Input: coins = [1], amount = 1
# Output: 1
#  
# 
#  Example 5: 
# 
#  
# Input: coins = [1], amount = 2
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= coins.length <= 12 
#  1 <= coins[i] <= 231 - 1 
#  0 <= amount <= 231 - 1 
#  
#  Related Topics Dynamic Programming 
#  👍 4944 👎 150


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize] * (amount + 1) #因为第一个初始化为0，所以要amount + 1个

        dp[0] = 0

        for i in range(amount + 1):
            if dp[i] == sys.maxsize: continue #就是说这类情况无法更亲dp【i】

            for coin in coins:
                if coin + i <= amount: #只有当coin + i比总的需要的amount小的时候才开始考虑后续
                    dp[coin + i] = min(dp[coin + i], dp[i] + 1)
        if dp[-1] == sys.maxsize: return -1 #如果到最后算完，dp的最后一个还没有更新，就说明无解
        return dp[-1] 

        
# leetcode submit region end(Prohibit modification and deletion)
