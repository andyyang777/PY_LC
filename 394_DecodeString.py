# Given an encoded string, return its decoded string. 
# 
#  The encoding rule is: k[encoded_string], where the encoded_string inside the 
# square brackets is being repeated exactly k times. Note that k is guaranteed to 
# be a positive integer. 
# 
#  You may assume that the input string is always valid; No extra white spaces, 
# square brackets are well-formed, etc. 
# 
#  Furthermore, you may assume that the original data does not contain any digit
# s and that digits are only for those repeat numbers, k. For example, there won't
#  be input like 3a or 2[4]. 
# 
#  
#  Example 1: 
#  Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
#  Example 2: 
#  Input: s = "3[a2[c]]"
# Output: "accaccacc"
#  Example 3: 
#  Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
#  Example 4: 
#  Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"
#  Related Topics Stack Depth-first Search 
#  👍 3583 👎 177


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def decodeString(self, s: str) -> str:
        curnum = 0
        curstring = ''

        stack = []
        for char in s:
            if char == '[':
                stack.append(curstring)
                stack.append(curnum)
                curstring = ''
                curnum = 0
            elif char ==']':
                prenum = stack.pop()
                prestring = stack.pop()
                curstring = prestring + prenum*curstring
            elif char.isdigit():
                curnum = curnum * 10 + int(char)
            else:
                curstring += char

        return curstring


        
# leetcode submit region end(Prohibit modification and deletion)
