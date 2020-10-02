# Given an arbitrary ransom note string and another string containing letters fr
# om all the magazines, write a function that will return true if the ransom note 
# can be constructed from the magazines ; otherwise, it will return false. 
# 
#  Each letter in the magazine string can only be used once in your ransom note.
#  
# 
#  
#  Example 1: 
#  Input: ransomNote = "a", magazine = "b"
# Output: false
#  Example 2: 
#  Input: ransomNote = "aa", magazine = "ab"
# Output: false
#  Example 3: 
#  Input: ransomNote = "aa", magazine = "aab"
# Output: true
#  
#  
#  Constraints: 
# 
#  
#  You may assume that both strings contain only lowercase letters. 
#  
#  Related Topics String 
#  👍 694 👎 209


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for i in range(len(magazine)):
            if magazine[i] in dic:
                dic[magazine[i]] += 1
            else:
                dic[magazine[i]] = 1
        for j in range(len(ransomNote)):
            if ransomNote[j] in dic and dic[ransomNote[j]] > 0:
                dic[ransomNote[j]] -= 1
            else:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
