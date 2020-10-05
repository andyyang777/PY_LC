# Given the head of a linked list, return the list after sorting it in ascending
#  order. 
# 
#  Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.
# e. constant space)? 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
#  
# 
#  Example 3: 
# 
#  
# Input: head = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 5 * 104]. 
#  -105 <= Node.val <= 105 
#  
#  Related Topics Linked List Sort 
#  👍 3198 👎 145


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        slow, fast = head, head.next

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        mid = slow.next
        slow.next = None

        left, right = self.sortList(head), self.sortList(mid)

        res = dummy = ListNode(0)

        while left and right:
            if left.val < right.val:
                dummy.next = left
                left = left.next
            else:
                dummy.next = right
                right = right.next
            dummy = dummy.next

        dummy.next = left if left else right

        return res.next


        
# leetcode submit region end(Prohibit modification and deletion)
