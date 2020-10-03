# You are given an array of k linked-lists lists, each linked-list is sorted in 
# ascending order. 
# 
#  Merge all the linked-lists into one sorted linked-list and return it. 
# 
#  
#  Example 1: 
# 
#  
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
#  
# 
#  Example 2: 
# 
#  
# Input: lists = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: lists = [[]]
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  k == lists.length 
#  0 <= k <= 10^4 
#  0 <= lists[i].length <= 500 
#  -10^4 <= lists[i][j] <= 10^4 
#  lists[i] is sorted in ascending order. 
#  The sum of lists[i].length won't exceed 10^4. 
#  
#  Related Topics Linked List Divide and Conquer Heap 
#  👍 5480 👎 309


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next      #############这个for的操作后，读的是list【i】的头节点，所以这个操作就可以把一整条链表读取完，从头开始读
        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next



# leetcode submit region end(Prohibit modification and deletion)
