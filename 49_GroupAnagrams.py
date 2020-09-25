# Given an array of strings strs, group the anagrams together. You can return th
# e answer in any order. 
# 
#  An Anagram is a word or phrase formed by rearranging the letters of a differe
# nt word or phrase, typically using all the original letters exactly once. 
# 
#  
#  Example 1: 
#  Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#  Example 2: 
#  Input: strs = [""]
# Output: [[""]]
#  Example 3: 
#  Input: strs = ["a"]
# Output: [["a"]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= strs.length <= 104 
#  0 <= strs[i].length <= 100 
#  strs[i] consists of lower-case English letters. 
#  
#  Related Topics Hash Table String 
#  👍 4078 👎 197


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dicts = {}

        for words in strs:
            sortedWords = "".join(sorted(words))
            if sortedWords not in dicts:
                dicts[sortedWords] = [words]
            else:
                dicts[sortedWords].append(words)
        res = []
        for i in dicts.values():
            res.append(i)
        return res



        
# leetcode submit region end(Prohibit modification and deletion)
