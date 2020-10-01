# Given a paragraph and a list of banned words, return the most frequent word th
# at is not in the list of banned words. It is guaranteed there is at least one wo
# rd that isn't banned, and that the answer is unique. 
# 
#  Words in the list of banned words are given in lowercase, and free of punctua
# tion. Words in the paragraph are not case sensitive. The answer is in lowercase.
#  
# 
#  
# 
#  Example: 
# 
#  
# Input: 
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-b
# anned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banne
# d.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= paragraph.length <= 1000. 
#  0 <= banned.length <= 100. 
#  1 <= banned[i].length <= 10. 
#  The answer is unique, and written in lowercase (even if its occurrences in pa
# ragraph may have uppercase symbols, and even if it is a proper noun.) 
#  paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
#  
#  There are no hyphens or hyphenated words. 
#  Words only consist of letters, never apostrophes or other punctuation symbols
# . 
#  
#  Related Topics String 
#  👍 758 👎 1760


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banset = set(banned)
        for _ in "!?',;.":
            paragraph = paragraph.replace(_, " ")
        count = Counter(word for word in paragraph.lower().split())

        ans, most = '', 0
        for word in count:
            if count[word] > most and word not in banset:
                ans, most = word, count[word]
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
