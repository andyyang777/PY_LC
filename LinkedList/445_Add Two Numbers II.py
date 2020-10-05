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
        # 建立两个分别用于记录l1和l2各个结点值的栈
        stack1 = []
        stack2 = []

        # push each value into the stack separately
        def push_stack(node, stack):
            while node:
                stack.append(node.val)
                node = node.next

        push_stack(l1, stack1)
        push_stack(l2, stack2)

        carry = 0
        res = None
        # 循环迭代，直到栈为空或者carry为空，如果有carry的话，都还要把carry加上的
        while stack1 or stack2 or carry:
            temp1, temp2 = 0, 0 # to store the pop value
            if stack1:
                temp1 = stack1.pop()
            if stack2:
                temp2 = stack2.pop()

            mod = (temp2 + temp1 + carry) % 10
            carry = (temp2 + temp1 + carry) // 10
            currnode = ListNode(mod)
            currnode.next = res
            res = currnode
        return res



# leetcode submit region end(Prohibit modification and deletion)
