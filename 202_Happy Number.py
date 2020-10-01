# Write an algorithm to determine if a number n is "happy". 
# 
#  A happy number is a number defined by the following process: Starting with an
# y positive integer, replace the number by the sum of the squares of its digits, 
# and repeat the process until the number equals 1 (where it will stay), or it loo
# ps endlessly in a cycle which does not include 1. Those numbers for which this p
# rocess ends in 1 are happy numbers. 
# 
#  Return True if n is a happy number, and False if not. 
# 
#  Example: 
# 
#  
# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
#  
#  Related Topics Hash Table Math 
#  👍 2462 👎 454


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            sum = 0
            while n > 0:
                n, rest = divmod(n, 10)
                sum += rest ** 2
            return sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = getNext(n)
        return n == 1


        
# leetcode submit region end(Prohibit modification and deletion)
