# A string S of lowercase English letters is given. We want to partition this st
# ring into as many parts as possible so that each letter appears in at most one p
# art, and return a list of integers representing the size of these parts. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it split
# s S into less parts.
#  
# 
#  
# 
#  Note: 
# 
#  
#  S will have length in range [1, 500]. 
#  S will consist of lowercase English letters ('a' to 'z') only. 
#  
# 
#  
#  Related Topics Two Pointers Greedy 
#  👍 3225 👎 132

#使用双指针法，还有就是dict与enumerate结合使用的要点


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = {char:indx for indx, char in enumerate(S)}

        l = 0
        r = 0
        res = []

        for indx, char in enumerate(S):
            r = max(r, d[char])
            if r == indx:
                res.append(r-l+1)
                l = indx +  1
        return res

        
# leetcode submit region end(Prohibit modification and deletion)
