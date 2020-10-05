# You are given two non-empty linked lists representing two non-negative integer
# s. The most significant digit comes first and each of their nodes contain a sing
# le digit. Add the two numbers and return it as a linked list. 
# 
#  You may assume the two numbers do not contain any leading zero, except the nu
# mber 0 itself. 
# 
#  Follow up: 
# What if you cannot modify the input lists? In other words, reversing the lists
#  is not allowed.
#  
# 
#  
# Example:
#  
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
#  
#  Related Topics Linked List 
#  👍 1677 👎 167


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        res = None
        carry = 0
        while s1 or s2 or carry:
            temp1 = 0 if not s1 else s1.pop()
            temp2 = 0 if not s2 else s2.pop()
            total = temp1 + temp2 + carry
            carry = total // 10
            mod = total % 10
            currnode = ListNode(mod)
            currnode.next = res
            res = currnode
        return res




# leetcode submit region end(Prohibit modification and deletion)
