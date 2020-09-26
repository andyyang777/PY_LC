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

        mem = {} #key is amount, so that when meeting the repeat amount, we will have the memory

        def helper(coins, amount) -> int:

            if amount in mem: return mem[amount]

            if amount == 0:
                mem[amount] = 0
                return 0

            res = sys.maxsize -1
            for coin in coins:
                if amount >= coin: # 只有当需要的总额比给的coin的面值大的时候才需要计算，否则直接pass
                    this_res = helper(coins, amount-coin)
                    if this_res == -1:
                        continue
                    else:
                        res = min(this_res + 1, res)

            if res == sys.maxsize-1: ##说明在coin里没办法组成amount需要的解，所以res还是那个最大值，不会变小
                mem[amount] = -1
                return -1

            mem[amount] = res
            return res

        return helper(coins,amount)


        
# leetcode submit region end(Prohibit modification and deletion)
