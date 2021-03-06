# 
# Given a non-empty string s, you may delete at most one character. Judge whethe
# r you can make it a palindrome.
#  
# 
#  Example 1: 
#  
# Input: "aba"
# Output: True
#  
#  
# 
#  Example 2: 
#  
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
#  
#  
# 
#  Note: 
#  
#  The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000. 
#  
#  Related Topics String 
#  👍 1921 👎 123


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.helper(s, i + 1, j) or self.helper(s, i, j - 1)
        return True

    def helper(self, s, head, tail):
        while head < tail:
            if s[head] == s[tail]:
                head += 1
                tail -= 1
            else:
                return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
