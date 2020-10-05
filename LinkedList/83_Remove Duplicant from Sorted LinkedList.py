# Given a sorted linked list, delete all duplicates such that each element appea
# r only once. 
# 
#  Example 1: 
# 
#  
# Input: 1->1->2
# Output: 1->2
#  
# 
#  Example 2: 
# 
#  
# Input: 1->1->2->3->3
# Output: 1->2->3
#  
#  Related Topics Linked List 
#  👍 1851 👎 121


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
# leetcode submit region end(Prohibit modification and deletion)
