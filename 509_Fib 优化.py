# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibon
# acci sequence, such that each number is the sum of the two preceding ones, start
# ing from 0 and 1. That is, 
# 
#  
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
#  
# 
#  Given N, calculate F(N). 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
#  
# 
#  Example 2: 
# 
#  
# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
#  
# 
#  Example 3: 
# 
#  
# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
#  
# 
#  
# 
#  Note: 
# 
#  0 ≤ N ≤ 30. 
#  Related Topics Array 
#  👍 781 👎 201


# leetcode submit region begin(Prohibit modification and deletion)


####时间复杂度：O(N)O(N)。
空间复杂度：O(1)O(1)，仅仅使用了 current，prev1，prev2。
class Solution:
    def fib(self, N: int) -> int:
        if N<=1: return N
        if N == 2: return 1
        current = 0
        pre1 = 1
        pre2 = 1

        for i in range(3,N+1):
            current = pre1 + pre2
            pre2 = pre1
            pre1 = current
        return current
        
# leetcode submit region end(Prohibit modification and deletion)
