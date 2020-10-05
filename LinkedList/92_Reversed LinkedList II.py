# Reverse a linked list from position m to n. Do it in one-pass. 
# 
#  Note: 1 ≤ m ≤ n ≤ length of list. 
# 
#  Example: 
# 
#  
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
#  
#  Related Topics Linked List 
#  👍 2763 👎 154


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:


###太难思考了，要结合着图自己画


    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        if m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head

        left, right = dummy, dummy

        for i in range(m-1):
            left = left.next
        for i in range(n):
            right = right.next

        new_left = left.next
        new_right = right.next
        pre = new_left
        curr = pre.next

        while curr != new_right:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp

        left.next = right
        new_left.next = new_right

        return dummy.next




        
# leetcode submit region end(Prohibit modification and deletion)
