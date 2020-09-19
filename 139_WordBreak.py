# Given a non-empty string s and a dictionary wordDict containing a list of non-
# empty words, determine if s can be segmented into a space-separated sequence of 
# one or more dictionary words. 
# 
#  Note: 
# 
#  
#  The same word in the dictionary may be reused multiple times in the segmentat
# ion. 
#  You may assume the dictionary does not contain duplicate words. 
#  
# 
#  Example 1: 
# 
#  
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pe
# n apple".
#              Note that you are allowed to reuse a dictionary word.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
#  
#  Related Topics Dynamic Programming 
#  👍 4952 👎 245


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            if dp[i]: #如果第i个位置是true，则说明可拼接，那么再把后面的也拼出来
                for word in wordDict:
                    if s[i:i+len(word)] == word:
                        dp[i + len(word)] = True
        return dp[-1]

        
# leetcode submit region end(Prohibit modification and deletion)
