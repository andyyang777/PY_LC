# Given a string, determine if it is a palindrome, considering only alphanumeric
#  characters and ignoring cases. 
# 
#  Note: For the purpose of this problem, we define empty string as valid palind
# rome. 
# 
#  Example 1: 
# 
#  
# Input: "A man, a plan, a canal: Panama"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: "race a car"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  s consists only of printable ASCII characters. 
#  
#  Related Topics Two Pointers String 
#  👍 1436 👎 3188


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #这个回文是对称来的，所以数字也要考虑的
        #并且这个例子里，空string也是算作对称的
        #看A man, a plan, a canal: Panama
        #去掉空格，逗号和：之后
        #AmanaplanacanalPanama
        #不看大小写，就能发现这个是围绕着c为中心对称的额
        s = s.lower()
        i = 0
        j = len(s) - 1

        while i<j: #不需要=，因为等于的时候两个指针是同一个值，所以必然会相等，没有意义
            if not (s[i].isalpha() or s[i].isdigit()):
                i += 1
                continue
            if not (s[j].isalpha() or s[j].isdigit()):
                j -= 1
                continue
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

        
# leetcode submit region end(Prohibit modification and deletion)
