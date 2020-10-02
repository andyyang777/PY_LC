# Write a function that reverses a string. The input string is given as an array
#  of characters char[]. 
# 
#  Do not allocate extra space for another array, you must do this by modifying 
# the input array in-place with O(1) extra memory. 
# 
#  You may assume all the characters consist of printable ascii characters. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#  
# 
#  
#  Example 2: 
# 
#  
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#  
#  
#  
#  Related Topics Two Pointers String 
#  👍 1685 👎 721


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s.reverse() #太赖皮了
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left+1, right-1)
        helper(0, len(s)-1)
# leetcode submit region end(Prohibit modification and deletion)
