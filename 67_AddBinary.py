# Given two binary strings, return their sum (also a binary string). 
# 
#  The input strings are both non-empty and contains only characters 1 or 0. 
# 
#  Example 1: 
# 
#  
# Input: a = "11", b = "1"
# Output: "100" 
# 
#  Example 2: 
# 
#  
# Input: a = "1010", b = "1011"
# Output: "10101" 
# 
#  
#  Constraints: 
# 
#  
#  Each string consists only of '0' or '1' characters. 
#  1 <= a.length, b.length <= 10^4 
#  Each string is either "0" or doesn't contain any leading zero. 
#  
#  Related Topics Math String 
#  👍 2110 👎 291


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        M,N = len(a), len(b)
        if M < N:
            a = "0" * (N-M) + a
        else:
            b = "0" * (M-N) + b

        stack1 = list(a)
        stack2 = list(b)
        res = ""
        carry = 0
        while stack1 and stack2:
            s1, s2 = stack1.pop(),stack2.pop()
            cursum = int(s1) + int(s2) + carry
            if cursum >= 2:
                cursum %= 2
                carry = 1
            else:
                carry = 0

            res = str(cursum) + res
        if carry:
            res = "1" + res
        return res

        
# leetcode submit region end(Prohibit modification and deletion)
