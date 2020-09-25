# You have an array of logs. Each log is a space delimited string of words. 
# 
#  For each log, the first word in each log is an alphanumeric identifier. Then,
#  either: 
# 
#  
#  Each word after the identifier will consist only of lowercase letters, or; 
#  Each word after the identifier will consist only of digits. 
#  
# 
#  We will call these two varieties of logs letter-logs and digit-logs. It is gu
# aranteed that each log has at least one word after its identifier. 
# 
#  Reorder the logs so that all of the letter-logs come before any digit-log. Th
# e letter-logs are ordered lexicographically ignoring identifier, with the identi
# fier used in case of ties. The digit-logs should be put in their original order.
#  
# 
#  Return the final order of the logs. 
# 
#  
#  Example 1: 
#  Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","l
# et3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig
# 2 3 6"]
#  
#  
#  Constraints: 
# 
#  
#  0 <= logs.length <= 100 
#  3 <= logs[i].length <= 100 
#  logs[i] is guaranteed to have an identifier, and a word after the identifier.
#  
#  
#  Related Topics String 
#  👍 750 👎 2262


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        nums = []

        for log in logs:
            logsplit = log.split(" ")
            if logsplit[1].isalpha():
                letters.append((" ".join(logsplit[1:]), logsplit[0]))
            else:
                nums.append(log)
        letters.sort()
        return [letter[1] + " " + letter[0] for letter in letters] + nums


            
# leetcode submit region end(Prohibit modification and deletion)
