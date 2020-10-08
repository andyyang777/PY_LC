# Given two strings s and t , write a function to determine if t is an anagram o
# f s. 
# 
#  Example 1: 
# 
#  
# Input: s = "anagram", t = "nagaram"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: s = "rat", t = "car"
# Output: false
#  
# 
#  Note: 
# You may assume the string contains only lowercase alphabets. 
# 
#  Follow up: 
# What if the inputs contain unicode characters? How would you adapt your soluti
# on to such case? 
#  Related Topics Hash Table Sort 
#  👍 1860 👎 150


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 长度不等，肯定不可能构成
        if len(s) != len(t):
            return False
        return sorted(s)  == sorted(t)

        
# leetcode submit region end(Prohibit modification and deletion)
