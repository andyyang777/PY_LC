# Given a string, find the first non-repeating character in it and return its in
# dex. If it doesn't exist, return -1. 
# 
#  Examples: 
# 
#  
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode"
# return 2.
#  
# 
#  
# 
#  Note: You may assume the string contains only lowercase English letters. 
#  Related Topics Hash Table String 
#  👍 2234 👎 122


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        count = Counter(s)
        for index, char in enumerate(s):
            if count[char] == 1:
                return index
        return -1

        
# leetcode submit region end(Prohibit modification and deletion)
