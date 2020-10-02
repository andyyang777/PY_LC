# Given a singly linked list L: L0→L1→…→Ln-1→Ln, 
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→… 
# 
#  You may not modify the values in the list's nodes, only nodes itself may be c
# hanged. 
# 
#  Example 1: 
# 
#  
# Given 1->2->3->4, reorder it to 1->4->2->3. 
# 
#  Example 2: 
# 
#  
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
#  
#  Related Topics Linked List 
#  👍 2474 👎 129


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    ### Complexity Analysis

Time complexity: \mathcal{O}(N)O(N). There are three steps here. To identify the middle node takes \mathcal{O}(N)O(N) time. 
    To reverse the second part of the list, one needs N/2N/2 operations. The final step, to merge two lists, requires N/2N/2 operations as well. 
    In total, that results in \mathcal{O}(N)O(N) time complexity.

Space complexity: \mathcal{O}(1)O(1), since we do not allocate any additional data structures.
    
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #边界条件，如果没有，就跳出，否则会提示说None没有属性next
        if not head:
            return
        
        #第一步，快慢指针找到中点，如果有两个重点则要第二个中点当作中点
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #第二步，把中点后面的一半reverse
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #第三步，把两个lists融合merge起来
        first, second = head, prev
        while second.next: # 因为上一步做reverse，是在中点后的second段做的，所以这里用second.next来判断
            tmp = first.next
            first.next = second
            first = tmp

            tmp = second.next
            second.next = first
            second = tmp
# leetcode submit region end(Prohibit modification and deletion)
