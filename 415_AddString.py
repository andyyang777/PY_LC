# Given two non-negative integers num1 and num2 represented as string, return th
# e sum of num1 and num2. 
# 
#  Note:
#  
#  The length of both num1 and num2 is < 5100. 
#  Both num1 and num2 contains only digits 0-9. 
#  Both num1 and num2 does not contain any leading zero. 
#  You must not use any built-in BigInteger library or convert the inputs to int
# eger directly. 
#  
#  Related Topics String 
#  👍 1193 👎 302


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        d = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

        res1, res2 = 0,0
        for x in num1:
            res1 = res1*10 + d[x]
        for x in num2:
            res2 = res2*10 + d[x]

        return str(res1 + res2)


        
# leetcode submit region end(Prohibit modification and deletion)
