# Remove all elements from a linked list of integers that have value val. 
# 
#  Example: 
# 
#  
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
#  
#  Related Topics Linked List 
#  👍 2029 👎 98


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        falseHead = ListNode(0)
        falseHead.next = head

        prev, curr = falseHead, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return falseHead.next
        
# leetcode submit region end(Prohibit modification and deletion)
